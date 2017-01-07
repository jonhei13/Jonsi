using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Web;

namespace Mooshak2._0.Services
{
    public class CompilerService
    {
        private IdentityManager Ident = new IdentityManager();
        private string RootDir = AppDomain.CurrentDomain.BaseDirectory;
        private string TempDir = AppDomain.CurrentDomain.BaseDirectory + "\\temp";
        private string UserDataDir = AppDomain.CurrentDomain.BaseDirectory + @"\userdata";

        /// <summary>
        /// Compiles the code that is needed for student to submit and also
        /// when teacher creates milestone.
        /// It also checks for memory errors before returning a compiled submission.
        /// </summary>
        public SubmissionViewModel Compile(SubmissionViewModel Sub)
        {
            var TheUser = Ident.GetUser(Sub.UserName);

            string UserDirectory = UserDataDir + "\\"+ TheUser.Id +"\\"+ Sub.AssignmentID +"\\"+ Sub.MilestoneID;
            string UserZip = UserDirectory +"\\"+ Sub.FilePath;
            string WorkTemp = UserDataDir + "\\temp\\" + TheUser.Id + "\\"+ Sub.MilestoneID;
            string DeleteTemp = WorkTemp;
            string MainCpp = WorkTemp + "\\main.cpp";
            var random = new Random();

            Sub.Output = "empty";

            // Checks if the file upload succeeded from the web page
            if (!Directory.Exists(UserDirectory))
            {
                return null;
                //return, user assignment not found.
            }
            // Checks if the zipfile exists that contains the project.
            if(!File.Exists(UserZip))
            {
                return null;
                //return, user Data not found
            }
            // creates a temporary folder to work in,
            // but if it already exists, then it is given
            // a random name to prevent folderpath conflicts.
            while (Directory.Exists(WorkTemp))
            {
                const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                var rand = new string(Enumerable.Repeat(chars, 6)
                  .Select(s => s[random.Next(s.Length)]).ToArray());
                WorkTemp = WorkTemp +"-"+ rand;
                MainCpp = WorkTemp + "\\main.cpp";
            }

            if (!Directory.Exists(WorkTemp))
            {
                Directory.CreateDirectory(WorkTemp);
            }

            
            try
            {
                // extracts the project from the user to temporary directory.
                ZipFile.ExtractToDirectory(UserZip, WorkTemp);
            }
            catch
            {
                //error extracting zip file
            }

            if (!File.Exists(MainCpp))
            {
                //main.cpp not found, seaching in sub folders.
                IEnumerable<string> dirs = Directory.EnumerateFiles(WorkTemp, "*", SearchOption.AllDirectories)
                .Where(x => x.Contains("main.cpp"));
                try
                {
                    if(dirs.Count() == 0)
                    {
                        return null;
                    }
                    MainCpp = new DirectoryInfo(dirs.First()).FullName;
                    WorkTemp = Path.GetDirectoryName(MainCpp);
                }
                catch
                {
                    return null;
                }
            }

            Process cpp = new Process();
            // This code compiles the project, should give back main.exe
            cpp.StartInfo.WorkingDirectory = WorkTemp;
            cpp.StartInfo.FileName = RootDir + "\\compiler\\bin\\mingw32-g++.exe";
            cpp.StartInfo.Arguments = "-o main \""+ MainCpp +"\"";
            cpp.StartInfo.UseShellExecute = false;
            cpp.StartInfo.RedirectStandardError = true;
            cpp.Start();
            string error = cpp.StandardError.ReadToEnd();
           // cpp.WaitForExit(1000 * 1);
            cpp.Close();
            cpp.Dispose();

            Sub.Output = error;
            // if there are no errors from the compiler, we continiou to run the main.exe
            if (error.Length == 0)
            {
                
                Process compiled = new Process();
                compiled.StartInfo.WorkingDirectory = WorkTemp;
                compiled.StartInfo.FileName = "\""+ WorkTemp + "\\main.exe\"";
                compiled.StartInfo.UseShellExecute = false;
                compiled.StartInfo.RedirectStandardOutput = true;
                compiled.StartInfo.RedirectStandardInput = true;

                compiled.Start();
                if (Sub.Input != null)
                {

                    File.WriteAllText(WorkTemp + "\\input.txt", Sub.Input);

                    // this reads the input parameters to the project, if there are any.
                    string command;
                    using (StreamReader sr = new StreamReader(WorkTemp + "\\input.txt"))
                    {
                        command = sr.ReadToEnd();
                    }

                    using (StreamWriter sw = compiled.StandardInput)
                    {
                        sw.Write(Sub.Input);
                    }
                }

                string output = null;

                // task sets time limit, if the program is on endless loop, or
                // is waiting for input, then it will move along after 10 seconds.
                Task task = Task.Run(() => output = compiled.StandardOutput.ReadToEnd());
                task.Wait(1000 * 10);
                if(!task.IsCompleted)
                {
                    compiled.Kill();
                    compiled.Close();
                    try
                    {   // multiple kill and close, 
                        // .kill and .close would not always work on first attempt.
                        compiled.Close();
                        compiled.Kill();
                        compiled.Dispose();
                    }
                    catch
                    {

                    }
                }

                Sub.Output = output;

                try
                {
                    // final try to stop main.exe
                    // main.exe should not be running here, 
                    // but if it is it should end in this code.
                    compiled.WaitForExit(1000 * 1);
                    compiled.Close();
                    compiled.Kill();
                    compiled.Dispose();
                }
                catch
                {

                }

                try
                {
                    // calls dr.memory function.
                    Sub.DrMemory = drmemory(WorkTemp, Sub.Input, UserZip);
                }
                catch{}

            }

            else
            {
                Sub.Error = error;
            }

            // delets temporary work folder
            // sometimes the code runs so fast and the compiler
            // is still using the folder, so we use while loop 
            // to try it multiple times.
            int count = 0;
            while (Directory.Exists(DeleteTemp) && count < 100)
            {
                try
                {
                    Directory.Delete(DeleteTemp, true);
                }
                catch
                {
                    //file is still locked, bug?
                }
                count++;
            }
            return Sub;
        }
        /// <summary>
        /// Dr.memory is a program we added to check for memory erros in
        /// C++ code.
        /// it returns an error if the solution from the student fails to
        /// release all allocated memory when the program ends.
        /// </summary>
        public string drmemory(string WorkTemp, string InputFile, string UserDirectory)
        {
            Process compiled = new Process();
            compiled.StartInfo.WorkingDirectory = WorkTemp;
            compiled.StartInfo.FileName = RootDir + "\\drmemory\\bin\\drmemory.exe";
            compiled.StartInfo.Arguments = " -batch -logdir \""+ WorkTemp + "\" -- \""+ WorkTemp + "\\main.exe\"";
            compiled.StartInfo.UseShellExecute = false;
            compiled.StartInfo.RedirectStandardOutput = true;
            compiled.StartInfo.RedirectStandardInput = true;
            compiled.Start();
            if (InputFile != null)
            {
                string command;
                using (StreamReader sr = new StreamReader(WorkTemp + "\\input.txt"))
                {
                    command = sr.ReadToEnd();
                }

                using (StreamWriter sw = compiled.StandardInput)
                {
                    sw.Write(command);
                }
            }
            try
            {
                compiled.WaitForExit(1000 * 1);
                compiled.Kill();
                compiled.Dispose();
            }
            catch
            {

            }

            Thread.Sleep(2000);

            // Finds the dr memory folder.
            IEnumerable<string> dirs = Directory.EnumerateDirectories(WorkTemp, "*", SearchOption.AllDirectories)
                .Where(x => x.Contains("DrMemory-main.exe"));

            string DrMemFolder = new DirectoryInfo(dirs.First()).Name;

            // reads the result.txt from drmemory to output and then returning it.
            string output;
            using (StreamReader sr = new StreamReader(WorkTemp + "\\" + DrMemFolder + "\\results.txt"))
            {
                output = sr.ReadToEnd();
            }
            return output;
        }
    }
}