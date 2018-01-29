using Mooshak2._0.Models;
using Mooshak2._0.Models.Entities;
using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Services
{
    public class TeacherService
    {
        private ApplicationDbContext _db;
        private AssignmentService AS = new AssignmentService(null);
        private IdentityManager Ident = new IdentityManager();

        private string RootDir = AppDomain.CurrentDomain.BaseDirectory;
        private string UserDataDir = AppDomain.CurrentDomain.BaseDirectory + @"\userdata";
        private string AssDataDir = AppDomain.CurrentDomain.BaseDirectory + @"\assdata";

        public TeacherService()
        {
            _db = new ApplicationDbContext();
        }
        /// <summary>
        /// Takes in assignmentviewmodel filled with information about new assignment
        /// and creates it in the database.
        /// </summary>
        public int CreateAssignment(AssignmentViewModel NewAss)
        {
            if (NewAss == null)
            {
                return 0;
            }
            var Ass = new Assignment();

            Ass.Name = NewAss.Name;
            Ass.CourseID = NewAss.CourseID;
            Ass.Hidden = NewAss.Hidden;
            Ass.StartDate = NewAss.StartDate;
            Ass.DueDate = NewAss.DueDate;
            Ass.FilePath = "";

            _db.Assignment.Add(Ass);
            _db.SaveChanges();
            Ass.FilePath = "\assdata\\" + Ass.ID;
            _db.SaveChanges();
            return Ass.ID;
        }
        /// <summary>
        /// Attaches files to assignment from the teacher. The user sees these files.
        /// etc PDF files with assignment information.
        /// </summary>
        public AssignmentViewModel UploadAssignmentFiles(int modelID, AssignmentViewModel model, IEnumerable<HttpPostedFileBase> files)
        {
            // loops trough all files the teacher wants to upload
            foreach(var file in files)
            { 
                // and then adds the files to the teacher directory.
            if (file != null)
                {
                    string UserDirectory = AssDataDir + "\\" + modelID;
                    model.FilePath = UserDirectory;

                    // checks if the teacher directory exists.
                    if (!Directory.Exists(UserDirectory))
                    {
                        Directory.CreateDirectory(UserDirectory);
                    }

                    var fileName = Path.GetFileName(file.FileName);
                    var path = UserDirectory + "\\" + fileName;

                    // checks if he is uploading the same file again.
                    if (File.Exists(path))
                    {
                        File.Delete(path);
                    }

                    // saves the file.
                    file.SaveAs(Path.GetFullPath(path));
                }
            }
            return model;

        }
        /// <summary>
        /// Edits values for existing assignment that is in the database.
        /// </summary>
        public void EditAssignment(AssignmentViewModel NewAss)
        {
            if(NewAss == null)
            {
                return;
            }
            var AssToEdit = _db.Assignment.Where(x => x.ID == NewAss.ID).SingleOrDefault();

            if(AssToEdit == null)
            {
                return;
            }

            AssToEdit.Name = NewAss.Name;
            AssToEdit.CourseID = NewAss.CourseID;
            AssToEdit.Hidden = NewAss.Hidden;
            AssToEdit.StartDate = NewAss.StartDate;
            AssToEdit.DueDate = NewAss.DueDate;
            AssToEdit.FilePath = NewAss.FilePath;

            _db.SaveChanges();
        }
        /// <summary>
        /// Creates new milestone in the database.
        /// </summary>
        public int CreateMilestone(MilestoneViewModel NewMile)
        {
            if (NewMile == null)
            {
                return 0;
            }
            var Mile = new Milestone();

            Mile.Name = NewMile.Name;
            Mile.Input = NewMile.Input;
            Mile.Output = NewMile.Output;
            Mile.Description = NewMile.Description;
            Mile.AssignmentID = NewMile.AssignmentID;
            Mile.CourseID = NewMile.CourseID;
            Mile.Percent = NewMile.Percent;

            _db.Milestone.Add(Mile);
            _db.SaveChanges();

            return Mile.ID;
        }
        /// <summary>
        /// Edits values for existing milestone that is in the database.
        /// </summary>
        public void EditMilestone(MilestoneViewModel NewMile)
        {
            if(NewMile == null)
            {
                return;
            }
            var MileToEdit = _db.Milestone.Where(x => x.ID == NewMile.ID).SingleOrDefault();

            MileToEdit.Name = NewMile.Name;
            MileToEdit.Input = NewMile.Input;
            MileToEdit.Output = NewMile.Output;
            MileToEdit.Description = NewMile.Description;
            MileToEdit.AssignmentID = NewMile.AssignmentID;
            MileToEdit.CourseID = NewMile.CourseID;
            MileToEdit.Percent = NewMile.Percent;

            _db.SaveChanges();
        }
        /// <summary>
        /// Deletes assignment from the database and all its milestones.
        /// </summary>
        public void DeleteAssignment(int AssID)
        {
            var AssToDelete = _db.Assignment.SingleOrDefault(x => x.ID == AssID);
            if (AssToDelete == null)
            {
                return;
            }
            // this is the assignment to delete.
            var ToDelete = AS.GetAssignmentByID(AssID);

            // and here we delete all the milestones it has.
            if(ToDelete.Milestones.Count > 0)
            {
                foreach(var Mile in ToDelete.Milestones)
                {
                    DeleteMilestone(Mile.ID);
                }
            }

            var delete = _db.Assignment.Remove(AssToDelete);
            _db.SaveChanges();
        }
        /// <summary>
        /// Delets a single milestone from the database.
        /// </summary>
        public void DeleteMilestone(int MileID)
        {
            var MileToDelete = _db.Milestone.SingleOrDefault(x => x.ID == MileID);
            if(MileToDelete == null)
            {
                return;
            }

            var delete = _db.Milestone.Remove(MileToDelete);
            _db.SaveChanges();
        }
        /// <summary>
        /// Function that uses the compiler, teacher uploads .zip that has
        /// code to create new milestone for the students to solve.
        /// Optionally input file can also be uploaded.
        /// </summary>
        public MilestoneViewModel CompileMilestoneUpload(MilestoneViewModel model, HttpPostedFileBase ZipFile, HttpPostedFileBase TxtFile)
        {
            var TheUser = Ident.GetUser(model.UserModel.Name);

            SubmissionViewModel SVM = new SubmissionViewModel();


            if (TxtFile != null)
            {
                // Reads the textfile into the model.
                string result = new StreamReader(TxtFile.InputStream).ReadToEnd();
                SVM.Input = result;
                model.Input = result;
            }

            if (ZipFile != null)
            {
                // The directory the milestone .zip file will be saved in.
                string UserDirectory = UserDataDir + "\\" + TheUser.Id + "\\" + model.AssignmentID + "\\" + model.ID;

                // creates the directory.
                if (!Directory.Exists(UserDirectory))
                {
                    Directory.CreateDirectory(UserDirectory);
                }

                var fileName = Path.GetFileName(ZipFile.FileName);
                var path = UserDirectory + "\\" + fileName;

                // If the teacher uploads the same .zip file again for a specific milestone
                // then it will be replaced.
                try
                {
                    if (File.Exists(path))
                    {
                        File.Delete(path);
                    }

                    ZipFile.SaveAs(Path.GetFullPath(path));
                }
                catch
                {
                    // user probably pressed upload twice, nothing to worry about.
                }

                SVM.UserName = model.UserModel.Name;
                SVM.AssignmentID = model.AssignmentID;
                SVM.MilestoneID = model.ID;
                SVM.FilePath = fileName;
                CompilerService CS = new CompilerService();

                // compiler service called.
                var compiled = CS.Compile(SVM);

                model.Output = compiled.Output;
                model.DrMemory = compiled.DrMemory;
            }
            return model;
        }
        /// <summary>
        /// Returns a list of all files the teacher uploaded for a specific milestone.
        /// These files are not the files the student sees.
        /// These are the files with the correct solution he uploaded to create the milestone.
        /// </summary>
        public List<string> GetMilestoneLinks(MilestoneViewModel Mile, string UserName)
        {
            var TheUser = Ident.GetUser(UserName);

            // the folder the data should be saved in.
            DirectoryInfo TeacherDataFolder =  new DirectoryInfo(UserDataDir + "\\" + TheUser.Id + "\\" + Mile.AssignmentID + "\\" + Mile.ID);
            List<string> ReturnList = new List<string>();
            List<System.IO.FileInfo> NameList = null;
            try
            {
                NameList = TeacherDataFolder.GetFiles().ToList();

                // fills the list with path to the files.
                foreach (var data in NameList)
                {
                    string adder = "\\userdata\\" + TheUser.Id + "\\" + Mile.AssignmentID + "\\" + Mile.ID + "\\" + data;
                    ReturnList.Add(adder);
                }
            }
            catch
            {
                //directory does not exist.
            }

            return ReturnList;
        }
        /// <summary>
        /// Files the teacher uploaded that goes with each assignment, both
        /// for the student and the teacher.
        /// etc pdf with assignment description.
        /// </summary>
        public List<string> GetAssignmentLinks(AssignmentViewModel model)
        {

            DirectoryInfo TeacherDataFolder = new DirectoryInfo(AssDataDir + "\\" + model.ID);
            List<string> ReturnList = new List<string>();
            List<System.IO.FileInfo> NameList = null;
            try
            {
                NameList = TeacherDataFolder.GetFiles().ToList();
                // cycles trough the directory and fills a list with
                // all the files.
                foreach (var data in NameList)
                {
                    string adder = "\\assdata\\" + "\\" + model.ID + "\\" + data;
                    ReturnList.Add(adder);
                }
            }
            catch
            {
                //directory does not exist.
            }

            return ReturnList;
        }
        /// <summary>
        /// Get all students and teachers that are linked to a specific course
        /// </summary>
        public List<UserViewModel> GetAllStudentsInCourse(int? CourseID)
        {
            var Users = (from Application in _db.Users
                         join C in _db.UserCourse on Application.UserName equals C.UserName
                         where C.CourseID == CourseID
                         select new UserViewModel()
                         {
                             UserName = Application.UserName,
                             ID = Application.Id,

                         }).ToList();
            return Users;
        }
        /// <summary>
        /// get all submissions for a specific milestone
        /// </summary>
        public List<SubmissionViewModel> GetSubmissionsInMilestone(int MilestoneID)
        {
            List<SubmissionViewModel> submissions = (from submission in _db.Submission
                               where submission.MilestoneID == MilestoneID
                               select new SubmissionViewModel
                               {
                                    ID = submission.ID,
                                    UserName = submission.UserName,
                                    AssignmentID = submission.AssignmentID,
                                    MilestoneID = submission.MilestoneID, 
                                    CourseID = submission.CourseID,
                                    Error = submission.Error,
                                    FilePath = submission.FilePath,
                                    Grade = submission.Grade,
                                    Status = submission.Status,
                                    ToSubmit = submission.ToSubmit,
                                    Comment = submission.Comment
                                }).ToList();
            return submissions;
        }
        /// <summary>
        /// Takes in filepath, and delets the file.
        /// </summary>
        public void DeleteAssignmentFile(string filepath)
        {
            string path = RootDir + filepath;
            File.Delete(path);
        }
        /// <summary>
        /// The function for teacher to comment and grade a submission for a student.
        /// </summary>
        public void TeacherComment(string comment, int SubID, double grade)
        {
            var Submission = _db.Submission.SingleOrDefault(x => x.ID == SubID);
            if(Submission == null)
            {
                throw new Exception();
            }
            Submission.Grade = grade;
            Submission.Comment = comment;
            _db.SaveChanges();
        }
    }
}