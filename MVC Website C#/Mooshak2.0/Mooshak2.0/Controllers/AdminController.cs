using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.EntityFramework;
using Mooshak2._0.Models;
using Mooshak2._0.Models.ViewModels;
using Mooshak2._0.Services;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Mail;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Web;
using System.Web.Mvc;

namespace Mooshak2._0.Controllers
{
    [Authorize(Roles = "Administrators")]
    public class AdminController : Controller
    {
        private AdminService AS = new AdminService();
        private AssignmentService ASS = new AssignmentService(null);
        private IdentityManager Ident = new IdentityManager();

        public ActionResult AdminHome()
        {
            UserService US = new UserService(null);
            var ViewModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), null);
            return View(ViewModel);
        }

        [HttpGet]
        public ActionResult CreateCourse()
        {
            return View();
        }
        /// <summary>
        /// Creates a course, can also take input from txt with teachers og students.
        /// The users that are in those textfiles are added to the course automatically
        /// and if they do not exist in the system they are created, and email is sent with password information to them.
        /// </summary>
        [HttpPost]
        public async Task<ActionResult> CreateCourse(CourseViewModel model, HttpPostedFileBase UsersFile, HttpPostedFileBase TeachersFile)
        {
            if (!ModelState.IsValid)
            {
                return View(model);
            }
            if (model.Name == null)
            {
                throw new Exception();
            }
            if (TeachersFile == null && UsersFile == null)
            {
                if (!ModelState.IsValid)
                {
                    throw new Exception();
                }
                AS.CreateCourse(model);
            }
            else if (UsersFile == null && TeachersFile != null)
            {
                model.ID = AS.CreateCourse(model);
                var SupportType = "txt";
                var FileText = System.IO.Path.GetExtension(TeachersFile.FileName).Substring(1);

                if (!SupportType.Contains(FileText))
                {
                    throw new Exception();
                }
                // Read the txt file take each word and link it to course
                string Result = new StreamReader(TeachersFile.InputStream).ReadToEnd();
                string[] lines = Regex.Split(Result, "\r\n");
                foreach (string word in lines)
                {
                    CreateUserViewModel NewUSer = new CreateUserViewModel();
                    NewUSer.Username = word.ToLower();
                    NewUSer.Password = AS.CreateRandomPassword();
                    NewUSer.Role = "Teachers";
                    NewUSer.CourseID = model.ID;
                    if (Ident.UserExists(NewUSer.Username))
                    {
                        UserViewModel New = AS.GetUserByName(NewUSer.Username);
                        New.CourseId = model.ID;
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {   //If user does not exist
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        string NewPassword = AS.CreateRandomPassword();
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(NewUSer.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + NewUSer.Username + "\n" + " Password: " + NewUSer.Password;
                        message.Body = string.Format(body, Email, NewUSer.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                        AS.CreateUser(NewUSer);
                        AS.LinkNewUserWithCourse(NewUSer);
                    }

                }
                model.ID = AS.CreateCourse(model);
            }
            else if (UsersFile != null && TeachersFile == null)
            {
                model.ID = AS.CreateCourse(model);
                var SupportType = "txt";
                var FileText = System.IO.Path.GetExtension(UsersFile.FileName).Substring(1);

                if (!SupportType.Contains(FileText))
                {
                    throw new Exception();
                }
                // Read the txt file take each word and link it to course
                string Result = new StreamReader(UsersFile.InputStream).ReadToEnd();
                string[] lines = Regex.Split(Result, "\r\n");
                foreach (string word in lines)
                {
                    CreateUserViewModel NewUSer = new CreateUserViewModel();
                    NewUSer.Username = word.ToLower();
                    NewUSer.Password = AS.CreateRandomPassword();
                    NewUSer.Role = "Students";
                    NewUSer.CourseID = model.ID;
                    if (Ident.UserExists(NewUSer.Username))
                    {
                        UserViewModel New = AS.GetUserByName(NewUSer.Username);
                        New.CourseId = model.ID;
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {   //If user does not exist
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        string NewPassword = AS.CreateRandomPassword();
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(NewUSer.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + NewUSer.Username + "\n" + " Password: " + NewUSer.Password;
                        message.Body = string.Format(body, Email, NewUSer.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                        AS.CreateUser(NewUSer);
                        AS.LinkNewUserWithCourse(NewUSer);
                    }

                }
            }
            else
            {
                model.ID = AS.CreateCourse(model);
                var SupportType = "txt";
                var FileText = System.IO.Path.GetExtension(UsersFile.FileName).Substring(1);

                if (!SupportType.Contains(FileText))
                {
                    throw new Exception();
                }
                // Read the txt file take each word and link it to course
                string Result = new StreamReader(UsersFile.InputStream).ReadToEnd();
                string[] lines = Regex.Split(Result, "\r\n");
                foreach (string word in lines)
                {
                    CreateUserViewModel NewUSer = new CreateUserViewModel();
                    NewUSer.Username = word.ToLower();
                    NewUSer.Password = AS.CreateRandomPassword();
                    NewUSer.Role = "Students";
                    NewUSer.CourseID = model.ID;
                    if (Ident.UserExists(NewUSer.Username))
                    {
                        UserViewModel New = AS.GetUserByName(NewUSer.Username);
                        New.CourseId = model.ID;
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {   //If user does not exist
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        string NewPassword = AS.CreateRandomPassword();
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(NewUSer.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + NewUSer.Username + "\n" + " Password: " + NewUSer.Password;
                        message.Body = string.Format(body, Email, NewUSer.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                        AS.CreateUser(NewUSer);
                        AS.LinkNewUserWithCourse(NewUSer);
                    }
                }
                var TeacherSupportType = "txt";
                var TeacherFileText = System.IO.Path.GetExtension(TeachersFile.FileName).Substring(1);

                if (!TeacherSupportType.Contains(FileText))
                {
                    throw new Exception();
                }
                // Read the txt file take each word and link it to course
                string TeacherResult = new StreamReader(TeachersFile.InputStream).ReadToEnd();
                string[] Teacherlines = Regex.Split(TeacherResult, "\r\n");
                foreach (string Teacherword in Teacherlines)
                {
                    CreateUserViewModel TeacherUser = new CreateUserViewModel();
                    TeacherUser.Username = Teacherword.ToLower();
                    TeacherUser.Password = AS.CreateRandomPassword();
                    TeacherUser.Role = "Teachers";
                    TeacherUser.CourseID = model.ID;
                    if (Ident.UserExists(TeacherUser.Username))
                    {
                        UserViewModel New = AS.GetUserByName(TeacherUser.Username);
                        New.CourseId = model.ID;
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {   //If user does not exist
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        string NewPassword = AS.CreateRandomPassword();
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(TeacherUser.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + TeacherUser.Username + "\n" + " Password: " + TeacherUser.Password;
                        message.Body = string.Format(body, Email, TeacherUser.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                        AS.CreateUser(TeacherUser);
                        AS.LinkNewUserWithCourse(TeacherUser);
                    }
                }
            }
            ModelState.Clear();
            var NewModel = new CourseViewModel();
            return View(NewModel);
        }

        [HttpGet]
        public ActionResult CreateUser()
        {
            var model = new CreateUserViewModel();
            model.Courses = AS.GetAllAvailableCourses();
            return View(model);
        }
        /// <summary>
        /// Creates a single user or with a list from textfile.
        /// The user can be added to the course automatically,
        /// if the user already exists that is in the .txt list, then no email is sent
        /// but the user is still added to the course.
        /// </summary>
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<ActionResult> CreateUser(CreateUserViewModel model, HttpPostedFileBase File)
        {
            if(!ModelState.IsValid)
            {
                model.Courses = AS.GetAllAvailableCourses();
                return View(model);
            }
            if (File == null)
            {
                if (ModelState.IsValid)
                {
                    model.Courses = AS.GetAllAvailableCourses();
                    model.Password = AS.CreateRandomPassword();
                    model.Email = model.Username;
                    model.Username = model.Username.ToLower();
                    if (Ident.UserExists(model.Username))
                    {
                        // user exists, he is added to the course, no email is sent.
                        UserViewModel New = AS.GetUserByName(model.Username);
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {
                        // User does not exist, so new one is created and email sent.
                        AS.CreateUser(model);
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(model.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + model.Username + "\n" + " Password: " + model.Password;
                        message.Body = string.Format(body, Email, model.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                    }
                }
            }
            else
            {
                var SupportType = "txt";
                var FileText = System.IO.Path.GetExtension(File.FileName).Substring(1);

                if (!SupportType.Contains(FileText))
                {
                    throw new Exception();
                }

                string Result = new StreamReader(File.InputStream).ReadToEnd();
                string[] lines = Regex.Split(Result, "\r\n");
                foreach (string word in lines)
                {

                    CreateUserViewModel NewUSer = new CreateUserViewModel();
                    model.Courses = AS.GetAllAvailableCourses();
                    NewUSer.Username = word.ToLower();
                    NewUSer.Password = AS.CreateRandomPassword();
                    NewUSer.Email = word;
                    NewUSer.Role = model.Role;
                    NewUSer.CourseID = model.CourseID;
                    if (Ident.UserExists(NewUSer.Username))
                    {
                        // user exists, he is added to the course, no email sent.
                        UserViewModel New = AS.GetUserByName(NewUSer.Username);
                        New.CourseId = NewUSer.CourseID;
                        AS.LinkUserWithCourse(New);
                    }
                    else
                    {
                        // user does not exist, he is created, added to the course, email sent.
                        AS.CreateUser(NewUSer);
                        string Email = ConfigurationManager.AppSettings["Email"];
                        string Password = ConfigurationManager.AppSettings["Password"];
                        var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
                        var message = new MailMessage();
                        message.To.Add(new MailAddress(NewUSer.Username));
                        message.From = new MailAddress(Email);
                        message.Subject = "Welcome To Mooshak 2.0";
                        string Informations = "Username: " + NewUSer.Username + "\n" + " Password: " + NewUSer.Password;
                        message.Body = string.Format(body, Email, model.Username, Informations);
                        message.IsBodyHtml = true;

                        using (var smtp = new SmtpClient())
                        {
                            var credential = new NetworkCredential
                            {
                                UserName = Email,
                                Password = Password
                            };
                            smtp.Credentials = credential;
                            smtp.Host = "smtp-mail.outlook.com";
                            smtp.Port = 587;
                            smtp.EnableSsl = true;
                            await smtp.SendMailAsync(message);
                        }
                    }
                }
            }
            ModelState.Clear();
            var NewModel = new CreateUserViewModel();
            NewModel.Courses = AS.GetAllAvailableCourses();
            return View(NewModel);
        }
        /// <summary>
        /// Edit a single user in the database.
        /// </summary>
        [HttpGet]
        public ActionResult EditUser(string UserID)
        {
            if (UserID != null)
            {
                UserViewModel model = new UserViewModel();
                IdentityManager Ident = new IdentityManager();
                model = Ident.GetEditedUser(UserID);
                if (model.UserName == null)
                {
                    throw new Exception();
                }
                model.Courses = AS.GetAllUserCourses(model.UserName).Courses;
                return View(model);
            }
            return null;

        }
        /// <summary>
        /// Removes a user from a specific course in the database.
        /// </summary>
        public ActionResult RemoveCourseFromUser(string Name, int? CourseID)
        {
            if (Name == null && !CourseID.HasValue)
            {
                throw new Exception();
            }
            AS.RemoveUserFromCourse(Name, CourseID.Value);

            return Redirect(Request.UrlReferrer.ToString());
        }
        /// <summary>
        /// deletes a course from the database.
        /// </summary>
        public ActionResult DeleteCourse(int? CourseID)
        {
            if (!CourseID.HasValue)
            {
                throw new Exception();
            }
            var Users = AS.UsersInCourse(CourseID.Value).Users;
            foreach (var U in Users)
            {
                AS.RemoveUserFromCourse(U.UserName, CourseID.Value);
            }
            AS.RemoveCourse(CourseID.Value);
            return Redirect(Request.UrlReferrer.ToString());
        }
        /// <summary>
        /// Edits a single user, email is sent to the new address if it is changed,
        /// and also password is sent to the new email address.
        /// </summary>
        [HttpPost]
        public async Task<ActionResult> EditUser(UserViewModel model)
        {
            if (!ModelState.IsValid)
            {
                var ViewModel = AS.GetAllUsersAndCourses();
                return View();
            }
            Ident.EditUser(model);
            string NewPassword = AS.CreateRandomPassword();
            string Email = ConfigurationManager.AppSettings["Email"];
            string Password = ConfigurationManager.AppSettings["Password"];
            var body = "<p>Email From: {0} ({1})</p><p>Message:</p><p>{2}</p>";
            var message = new MailMessage();
            message.To.Add(new MailAddress(model.UserName));
            message.From = new MailAddress(Email);
            message.Subject = "Welcome To Mooshak 2.0";
            string Informations = "Username: " + model.UserName + "\n" + " Password: " + NewPassword;
            message.Body = string.Format(body, Email, model.UserName, Informations);
            message.IsBodyHtml = true;
            using (var smtp = new SmtpClient())
            {
                var credential = new NetworkCredential
                {
                    UserName = Email,
                    Password = Password
                };
                smtp.Credentials = credential;
                smtp.Host = "smtp-mail.outlook.com";
                smtp.Port = 587;
                smtp.EnableSsl = true;
                await smtp.SendMailAsync(message);
            }
        
            return RedirectToAction("AllStudents");
        }

        [HttpGet]
        public ActionResult EditCourse(int? CourseID)
        {
            if (!CourseID.HasValue || !ASS.CourseExist(CourseID))
            {
                throw new Exception();
            }
            var Model = AS.GetCourse(CourseID.Value);
            return View(Model);

        }

        [HttpPost]
        public ActionResult EditCourse(CourseViewModel model)
        {
            if (!ModelState.IsValid)
            {
                return View(model);
            }
            AS.EditCourse(model);
            return RedirectToAction("AllCourses");
        }
        /// <summary>
        /// Delets a user from the database,
        /// </summary>
        public ActionResult DeleteUser(string UserID, int? CourseID)
        {
            if (UserID == null)
            {
                throw new Exception();
            }
            string Role = Ident.GetUserRole(UserID);
            if (Role == "Students")
            {
                AS.DeleteUser(UserID);
                if (!CourseID.HasValue)
                { 
                    return RedirectToAction("AllStudents");
                }
                else
                { 
                    return RedirectToAction("UsersInCourse", new { CourseID = CourseID });
                }
            }
            else if (Role == "Teachers")
            {
                AS.DeleteUser(UserID);
                if (!CourseID.HasValue)
                {
                    return RedirectToAction("AllTeachers");
                }
                else
                {
                    return RedirectToAction("UsersInCourse", new { CourseID = CourseID });
                }
            }
            else if (Role == "Admins")
            {
                AS.DeleteUser(UserID);
                if (!CourseID.HasValue)
                {
                    return RedirectToAction("AllAdmins");
                }
                else
                {
                    return RedirectToAction("UsersInCourse", new { CourseID = CourseID });
                }
            }
            return RedirectToAction("ErrorDelete");
        }
        /// <summary>
        /// Retrieves a list of all students and teachers that
        /// are enrolled or teaching specific course.
        /// </summary>
        [HttpGet]
        public ActionResult UsersInCourse(int? CourseID, string SearchString)
        {
            if (!CourseID.HasValue || !ASS.CourseExist(CourseID))
            {
                throw new Exception();
            }
            var ViewModel = AS.UsersInCourse(CourseID.Value);
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Users = ViewModel.Users.Where(x => x.UserName.Contains(SearchString)).ToList();
            }
            return View(ViewModel);
        }

        /// <summary>
        /// Link student or teacher to a course.
        /// </summary>
        [HttpGet]
        public ActionResult LinkUserToCourses(string Name, string SearchString)
        {
            if (Name == null)
            {
                throw new Exception();
            }

            var Courses = AS.GetOnlyCoursesUserIsNotIn(Name);
            var ViewModel = AS.GetUserByName(Name);
            if(ViewModel == null)
            {
                throw new Exception();
            }
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Courses = ViewModel.Courses.Where(x => x.Name.Contains(SearchString)).ToList();
            }
            else
            {
                ViewModel.Courses = Courses;
            }

            return View(ViewModel);
        }

        [HttpPost]
        public ActionResult LinkUserToCourses(UserViewModel Model)
        {
            if(!ModelState.IsValid)
            {
                return View(Model);
            }
            for (var i = 0; i < Model.Courses.Count(); i++)
            {
                if (Model.Courses[i].IsSelected)
                {
                    Model.CourseId = Model.Courses[i].ID;
                    AS.LinkUserWithCourse(Model);
                }
            }
            return RedirectToAction("AdminHome");
        }
        /// <summary>
        /// You can choose users in a list with checkboxes in existing course
        ///  to add to another course
        /// </summary>
        [HttpGet]
        public ActionResult LinkAllUsersInCourseToAnother(int? CourseID, string SearchString)
        {
            if (!CourseID.HasValue || !ASS.CourseExist(CourseID))
            {
                throw new Exception();
            }

            var Courses = AS.GetAllUsersAndCourses().Courses;
            var Users = AS.UsersInCourse(CourseID.Value).Users;
            var ViewModel = new AdminHomeViewModel()
            {
                Courses = Courses,
                Users = Users,
                CourseName = AS.GetCourseByID(CourseID.Value).Name
            };  

            return View(ViewModel);
        }

        [HttpPost]
        public ActionResult LinkAllUsersInCourseToAnother(AdminHomeViewModel Model)
        {
            if(!ModelState.IsValid)
            {
                return View(Model);
            }
            for (var i = 0; i < Model.Courses.Count(); i++)
            {
                if (Model.Courses[i].IsSelected)
                {
                    for (var k = 0; k < Model.Users.Count(); k++)
                    {
                        if (Model.Users[k].IsSelected)
                        {
                            var NewLink = new UserViewModel()
                            {
                                UserName = Model.Users[k].UserName,
                                CourseId = Model.Courses[i].ID,
                            };
                            AS.LinkUserWithCourse(NewLink);
                        }
                    }
                }
            }
            return RedirectToAction("AllCourses");
        }
        /// <summary>
        /// Returns list of all students, or filtered with search string.
        /// </summary>
        [HttpGet]
        public ActionResult AllStudents(string SearchString)
        {
            var ViewModel = AS.GetAllUsersAndCourses();
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Users = ViewModel.Users.Where(x => x.UserName.Contains(SearchString)).ToList();
            }
            return View(ViewModel);
        }
        /// <summary>
        /// Returns list of all teachers, or filtered with search string.
        /// </summary>
        [HttpGet]
        public ActionResult AllTeachers(string SearchString)
        {
            var ViewModel = AS.GetAllUsersAndCourses();
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Users = ViewModel.Users.Where(x => x.UserName.Contains(SearchString)).ToList();
            }
            return View(ViewModel);
        }
        /// <summary>
        /// Returns list of all courses, or filtered with search string.
        /// </summary>
        [HttpGet]
        public ActionResult AllCourses(string SearchString)
        {
            var ViewModel = AS.GetAllUsersAndCourses();
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Courses = ViewModel.Courses.Where(x => x.Name.Contains(SearchString)).ToList();
            }
            return View(ViewModel);
        }
        /// <summary>
        /// Returns list of all admins, or filtered with search string.
        /// </summary>
        [HttpGet]
        public ActionResult AllAdmins(string SearchString)
        {
            var ViewModel = AS.GetAllUsersAndCourses();
            if (!string.IsNullOrEmpty(SearchString))
            {
                ViewModel.Users = ViewModel.Users.Where(x => x.UserName.Contains(SearchString)).ToList();
            }
            return View(ViewModel);
        }
    }
}