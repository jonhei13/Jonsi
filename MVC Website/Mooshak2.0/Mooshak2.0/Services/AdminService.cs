using Mooshak2._0.Models;
using Mooshak2._0.Models.Entities;
using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Net.Mail;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.Mvc;

namespace Mooshak2._0.Services
{
    public class AdminService
    {
        private ApplicationDbContext _db = new ApplicationDbContext();
        private IdentityManager Ident = new IdentityManager();
        private const int PASSWORDLENGTH = 8;

        public object AccountViewModels { get; private set; }

        /// <summary>
        /// Gets a single user from database and returns username and role.
        /// </summary>
        public UserViewModel GetUserByName(string userName)
        {
            var User = _db.Users.SingleOrDefault(x => x.UserName == userName);

            if (User == null)
            {
                return null;
            }
            var ViewModel = new UserViewModel
            {
                UserName = User.UserName,
                Role = Ident.GetUserRole(User.Id),
            };

            return ViewModel;
        }

        /// <summary>
        /// Creates a single new user
        /// </summary>
        public void CreateUser(CreateUserViewModel Create)
        {
            if (!Ident.UserExists(Create.Username))
            {
                ApplicationUser CreateUser = new ApplicationUser();

                CreateUser.UserName = Create.Username;
                CreateUser.Email = Create.Username;
                if (!Ident.CreateUser(CreateUser, Create.Password))
                {
                    throw new Exception();
                }

                if (!Ident.AddUserToRole(CreateUser.Id, Create.Role))
                {
                    throw new Exception();
                }
                LinkNewUserWithCourse(Create);

            }
        }


        /// <summary>
        ///  Links a new created user with a course that already exists.
        /// </summary>
        public void LinkNewUserWithCourse(CreateUserViewModel CreateUser)
        {
            var IfUserExist = _db.UserCourse.SingleOrDefault(x => x.UserName == CreateUser.Username && x.CourseID == CreateUser.CourseID);
            if (IfUserExist == null)
            {
                UserCourse LinkStudentAndCourse = new UserCourse();
                LinkStudentAndCourse.CourseID = CreateUser.CourseID;
                LinkStudentAndCourse.UserName = CreateUser.Username;
                _db.UserCourse.Add(LinkStudentAndCourse);
                _db.SaveChanges();
            }
        }
        /// <summary>
        /// Links a user with course that already exists 
        /// </summary>
        public void LinkUserWithCourse(UserViewModel Model)
        {
            var IfUserExist = _db.UserCourse.SingleOrDefault(x => x.UserName == Model.UserName && x.CourseID == Model.CourseId);
            if (IfUserExist == null)
            {
                UserCourse LinkStudentAndCourse = new UserCourse();
                LinkStudentAndCourse.CourseID = Model.CourseId;
                LinkStudentAndCourse.UserName = Model.UserName;
                _db.UserCourse.Add(LinkStudentAndCourse);
                _db.SaveChanges();

            }
       


        }
        /// <summary>
        /// Returns a single course 
        /// </summary>
        public CourseViewModel GetCourseByID(int CourseID)
        {

            var Course = _db.Course.SingleOrDefault(x => x.ID == CourseID);
            if (Course == null)
            {
                throw new Exception();
            }

            var ViewModel = new CourseViewModel
            {
                Name = Course.Name,
                ID = Course.ID
            };
            return ViewModel;
        }
        /// <summary>
        /// Returns all users from database
        /// </summary>
        public AdminHomeViewModel GetAllUserCourses(string UserName)
        {
            var OverviewUserinCourse = (from Application in _db.Course
                                        join C in _db.UserCourse on Application.ID equals C.CourseID
                                        where C.UserName == UserName
                                        select new CourseViewModel()
                                        {
                                            Name = Application.Name,
                                            ID = Application.ID

                                        }).ToList();
            var ViewModel = new AdminHomeViewModel()
            {
                Courses = OverviewUserinCourse
            };

            return ViewModel;
        }
        /// <summary>
        /// Returns all userrs and courses from database
        /// </summary>
        public AdminHomeViewModel GetAllUsersAndCourses()
        {
            var AllCourses = _db.Course
                .Select(x => new CourseViewModel
                {
                    Name = x.Name,
                    ID = x.ID
                })
            .ToList();

            var AllUsers = _db.Users
                .AsEnumerable()
                .Select(x => new UserViewModel
                {

                    UserName = x.UserName,
                    Role = Ident.GetUserRole(x.Id),
                    ID = x.Id

                }).ToList();

            var ViewModel = new AdminHomeViewModel
            {
                Users = AllUsers,
                Courses = AllCourses,
            };
            return ViewModel;
        }
        /// <summary>
        /// Creates a new course in the database
        /// </summary>
        public int CreateCourse(CourseViewModel CreateCourse)
        {
            var IfExist = _db.Course.SingleOrDefault(x => x.Name == CreateCourse.Name);
            if (IfExist != null)
            {
                throw new Exception();
            }

            var Course = new Course();
            Course.Name = CreateCourse.Name;
            _db.Course.Add(Course);
            _db.SaveChanges();

            return Course.ID;
        }
        /// <summary>
        /// Returns selected course
        /// </summary>
        public CourseViewModel GetCourse(int ID)
        {
            var Course = _db.Course.SingleOrDefault(x => x.ID == ID);

            if(Course == null)
            {
                return null;
            }
            var ViewModel = new CourseViewModel
            {
                Name = Course.Name,
                ID = Course.ID,
            };
            return ViewModel;
        }
        /// <summary>
        /// Get all courses from the database
        /// </summary>
        public List<SelectListItem> GetAllAvailableCourses()
        {
            List<SelectListItem> Courses = new List<SelectListItem>();

            Courses.Add(new SelectListItem() { Value = "", Text = "- Choose a Course" });

            _db.Course.ToList().ForEach((x) =>
            {
                Courses.Add(new SelectListItem() { Value = x.ID.ToString(), Text = x.Name });
            });

            return Courses;
        }
        /// <summary>
        /// Creates random password, used in creating account.
        /// </summary>
        public string CreateRandomPassword()
        {
            string allowedChars = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0123456789!@$?_-";
            char[] chars = new char[PASSWORDLENGTH];
            Random rd = new Random();

            for (int i = 0; i < PASSWORDLENGTH; i++)
            {
                chars[i] = allowedChars[rd.Next(0, allowedChars.Length)];
            }

            return new string(chars);
        }
        /// <summary>
        /// Edits a course in the database
        /// </summary>
        public void EditCourse(CourseViewModel Model)
        {
            var EditCourse = _db.Course.SingleOrDefault(x => x.ID == Model.ID);
            EditCourse.Name = Model.Name;
            _db.SaveChanges();
        }
        /// <summary>
        /// Returns all users that are in the selected Course
        /// </summary>
        public AdminHomeViewModel UsersInCourse(int CourseID)
        {   //Select all users from database with the given courseID
            var UsersInCourse = (from Application in _db.Users
                                 join C in _db.UserCourse on Application.UserName equals C.UserName
                                 where C.CourseID == CourseID
                                 select new UserViewModel()
                                 {
                                     UserName = Application.UserName,
                                     ID = Application.Id,

                                 }).ToList();
            foreach (var User in UsersInCourse)
            {
                User.Role = Ident.GetUserRole(User.ID);
            }
            var ViewModel = new AdminHomeViewModel()
            {
                Users = UsersInCourse,
                CourseID = CourseID,
                CourseName = GetCourseByID(CourseID).Name
            };
            return ViewModel;
        }
        /// <summary>
        /// Deleets a specific user from the database,
        /// all the user data has to be deleted before the
        /// use us deleted.
        /// </summary>
        public void DeleteUser(string UserID)
        {
            var User = _db.Users.SingleOrDefault(x => x.Id == UserID);
            var DeleteUserSubmissions = _db.Submission.Where(x => x.UserName == User.UserName).ToList();
            var DeleteUserInCourse = _db.UserCourse.Where(x => x.UserName == User.UserName).ToList();


            foreach (var Sub in DeleteUserSubmissions)
            {
                _db.Submission.Remove(Sub);
            }
            _db.SaveChanges();
            foreach (var UserInCourse in DeleteUserInCourse)
            {
                _db.UserCourse.Remove(UserInCourse);
            }
            _db.SaveChanges();
            Ident.DeleteUser(User.Id);
            _db.SaveChanges();
        }
        /// <summary>
        /// Removes specific user from a course in the database
        /// </summary>
        public void RemoveUserFromCourse(string Name, int CourseID)
        {
            var User = Ident.GetUser(Name);
            var RemoveUser = (from Application in _db.UserCourse
                              where Application.CourseID == CourseID && Application.UserName == Name
                              select Application).ToList();
            foreach (var R in RemoveUser)
            {
                _db.UserCourse.Remove(R);
                _db.SaveChanges();
            }
        
        }
        /// <summary>
        /// Get all the courses that give user is not in.
        /// </summary>
        public List<CourseViewModel> GetOnlyCoursesUserIsNotIn(string Name)
        {
            
            var Courses = (from Application in _db.UserCourse
                           join C in _db.UserCourse on Application.UserName equals C.UserName
                           where Application.UserName == Name
                           select new CourseViewModel
                           {
                               ID = Application.CourseID,
                               
                           }).ToList();

            var AllCourses = (from Application in _db.Course
                              select new CourseViewModel
                              {
                                  Name = Application.Name,
                                  ID = Application.ID

                              }).ToList();
            //Finds the all the courses user is in and removes to display.
           for (var i = 0; i < Courses.Count(); i++)
            {
                for (var k = 0; k < AllCourses.Count(); k++)
                {
                    if (AllCourses[k].ID == Courses[i].ID)
                    {
                        AllCourses.Remove(AllCourses[k]);
                    }
                }
            }
            return AllCourses;
        }
        /// <summary>
        /// Removes a course from the database
        /// </summary>
        public void RemoveCourse(int CourseID)
        {
            var Submissions = _db.Submission.Where(x => x.CourseID == CourseID).ToList();
            var MileStones = _db.Milestone.Where(x => x.CourseID == CourseID).ToList();
            var Assignments = _db.Assignment.Where(x => x.CourseID == CourseID).ToList();
            var Course = _db.Course.SingleOrDefault(x => x.ID == CourseID);
            foreach (var Sub in Submissions)
            {
                _db.Submission.Remove(Sub);
            }
            _db.SaveChanges();
            foreach(var Mile in MileStones)
            {
                _db.Milestone.Remove(Mile);
            }
            _db.SaveChanges();
            foreach(var Assign in Assignments)
            {
                _db.Assignment.Remove(Assign);
            }
            _db.SaveChanges();
            _db.Course.Remove(Course);
            _db.SaveChanges();
        }
    }


}