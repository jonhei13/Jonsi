using Mooshak2._0.Models;
using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Services
{
    public class UserService
    {
        private AssignmentService AS = new AssignmentService(null);
        private SubmissionService SS = new SubmissionService(null);
        private IdentityManager Ident = new IdentityManager();
        private AdminService AMS = new AdminService();
        private readonly IAppDataContext _db;

        public UserService(IAppDataContext dbContext)
        {
            _db = dbContext ?? new ApplicationDbContext();
        }


        private string RootDir = AppDomain.CurrentDomain.BaseDirectory;
        private string UserDataDir = AppDomain.CurrentDomain.BaseDirectory + @"\userdata";


        /// <summary>
        /// Get all basic data for the user,
        /// all  assignments, milestones and submissions for a specific course
        /// </summary>
        public UserHomeViewModel GetUserOverviewByUserName(string UserName, int? CourseID)
        {
            // first, finds all the courses.
            var UserCourses = (from Course in _db.Course
                                  join Connection in _db.UserCourse
                                  on Course.ID equals Connection.CourseID
                                  where Connection.UserName == UserName
                                  select new CourseViewModel
                                  {
                                      ID = Course.ID,
                                      Name = Course.Name
                                  }).ToList();
            // if courseID is null, and the user is enrolled in a course, 
            // then we return the first course by default.
            if(CourseID == null && UserCourses.Count> 0)
            {
                CourseID = UserCourses[0].ID;
            }

            // finally fill the viewmodel and then return it.
            var ViewModel = new UserHomeViewModel
            {
                Name = UserName,
                UserID = AMS.GetUserByName(UserName).ID,
                CourseID = CourseID,
                Courses = UserCourses,
                Assignments = AS.GetAssignmentsByCourseID(CourseID),
                Submissions = SS.GetUserSubmissionsByCourseID(UserName, CourseID)
            };
            if(CourseID.HasValue)
            {
                ViewModel.CourseName = AMS.GetCourseByID(CourseID.Value).Name;
            }
            return ViewModel;

        }
        /// <summary>
        /// A function that users the compiler when the student uploads assignment,
        /// very similar to the milestone compile function that the teacher uses.
        /// </summary>
        public SubmissionViewModel StudentCompile(MilestoneViewModel model, HttpPostedFileBase ZipFile)
        {
            var TheUser = Ident.GetUser(model.UserModel.Name);
            int Count = 1;
            var Compiled = new SubmissionViewModel();
            var ToCompile = new SubmissionViewModel();

            if(model.Output == null)
            {
                throw new Exception();
            }
            if (ZipFile != null)
            {
                string UserDirectory = UserDataDir + "\\" + TheUser.Id + "\\" + model.AssignmentID + "\\" + model.ID + "\\" + Count;

                // with each submission we create a new folder with increasing number in the name
                while (Directory.Exists(UserDirectory))
                {
                    Count++;
                    UserDirectory = UserDataDir + "\\" + TheUser.Id + "\\" + model.AssignmentID + "\\" + model.ID + "\\" + Count;
                }

                Directory.CreateDirectory(UserDirectory);

                // we splice a couple of filepaths together to get the userdirectory and
                // zip directory so the compiler knows where to work.
                var fileName = Path.GetFileName(ZipFile.FileName);
                var path = UserDirectory + "\\" + fileName;
                string NewPath = UserDirectory + "\\" + model.UserModel.Name + "-" + model.ID + ".zip";

                try
                {
                    if (File.Exists(path))
                    {
                        File.Delete(path);
                    }
                    // saves the zip in user storage
                    ZipFile.SaveAs(Path.GetFullPath(path));

                    System.IO.File.Move(path, NewPath);
                    fileName = model.UserModel.Name + "-" + model.ID + ".zip";
                }
                catch
                {
                    // user probably pressed upload twice, nothing to worry about.
                }

                ToCompile.UserName = model.UserModel.Name;
                ToCompile.AssignmentID = model.AssignmentID;
                ToCompile.MilestoneID = model.ID;
                ToCompile.FilePath = Count +"\\"+ fileName;
                ToCompile.Input = model.Input;

                CompilerService CS = new CompilerService();
                // compiler called.
                Compiled = CS.Compile(ToCompile);

                ToCompile.FilePath = "\\userdata\\" + TheUser.Id + "\\" + model.AssignmentID + "\\" + model.ID + "\\" + Count + "\\" + fileName;
                ToCompile.Error = Compiled.Error;
                ToCompile.Output = Compiled.Output;
                ToCompile.DrMemory = Compiled.DrMemory;
                ToCompile.Status = Compiled.Status;
                ToCompile.AssignmentName = AS.GetAssignmentByID(model.AssignmentID).Name;
                ToCompile.CourseID = model.CourseID;

                if(ToCompile.Output == null)
                {
                    ToCompile.Output = "No output obtained";
                }
                if (ToCompile.DrMemory == null)
                {
                    ToCompile.DrMemory = "No memory file found";
                }
            }
            return ToCompile;
        }
    }
}