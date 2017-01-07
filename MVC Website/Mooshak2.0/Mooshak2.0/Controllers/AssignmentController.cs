using Microsoft.AspNet.Identity;
using Mooshak2._0.Models.ViewModels;
using Mooshak2._0.Services;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Security.AccessControl;
using System.Web;
using System.Web.Mvc;



namespace Mooshak2._0.Controllers
{
    public class AssignmentController : Controller
    {
        private TeacherService TS = new TeacherService();
        private UserService US = new UserService(null);
        private AssignmentService AS = new AssignmentService(null);
        private SubmissionService SS = new SubmissionService(null);
        private LevenshteinService LS = new LevenshteinService();

        private string RootDir = AppDomain.CurrentDomain.BaseDirectory;
        private string UserDataDir = AppDomain.CurrentDomain.BaseDirectory + @"\userdata";

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult CreateAssignment(int? CourseID)
        {
            if(CourseID != null)
            {
                if(!AS.CourseExist(CourseID))
                {
                    throw new Exception();
                }
            }
            var AssignmentViewModel = new AssignmentViewModel();
            AssignmentViewModel.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), CourseID);
            return View(AssignmentViewModel);
        }

        [HttpPost]
        [Authorize(Roles = "Teachers")]
        public ActionResult CreateAssignment(AssignmentViewModel model, IEnumerable<HttpPostedFileBase> files)
        {
            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);

            if (ModelState.IsValid)
            {
                ModelState.Clear();
                int AssID = TS.CreateAssignment(model);
                model = TS.UploadAssignmentFiles(AssID, model, files);
                return RedirectToAction("StudentAssignments", "User", new { id = AssID });
            }
            return View(model);
        }
        /// <summary>
        /// Teacher creates a new milestone for assignment
        /// sends in .zip with the program (main.cpp) and .txt with input if there is any.
        /// gets in return values from the compiler.
        /// </summary>
        [HttpPost]
        [Authorize(Roles = "Teachers")]
        public ActionResult CreateMilestone(MilestoneViewModel model, HttpPostedFileBase ZipFile, HttpPostedFileBase TxtFile)
        {
            if (ModelState.IsValid)
            {
                ModelState.Clear();
                int MileID = TS.CreateMilestone(model);
                model.ID = MileID;
                if (ZipFile != null)
                {
                    var ZipType = "zip";
                    var TextType = "txt";

                    var ZipEnding = System.IO.Path.GetExtension(ZipFile.FileName).Substring(1);
                    if (!ZipType.Contains(ZipEnding))
                    {
                        ViewBag.Output = "Error: upload approriate .zip file";
                        model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
                        return View(model);
                    }
                    if (TxtFile != null)
                    {
                        var TextEnding = System.IO.Path.GetExtension(TxtFile.FileName).Substring(1);
                        if (!TextType.Contains(TextEnding))
                        {
                            ViewBag.Output = "Error: upload approriate .txt file";
                            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
                            return View(model);
                        }
                    }
                    Stopwatch watch = new Stopwatch();
                    watch.Start();

                    try
                    {
                        model = TS.CompileMilestoneUpload(model, ZipFile, TxtFile);
                    }
                    catch
                    {
                        //return error, compile failed, invalid file?
                        throw new Exception();
                    }

                    watch.Stop();
                    TimeSpan ts = watch.Elapsed;
                    ViewBag.Output = "Compiled in " + ts.Seconds + "." + ts.Milliseconds / 10 + " seconds";

                    TS.EditMilestone(model);
                }
            }
            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
            return View(model);
        }

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult CreateMilestone(int AssignmentID, int? CourseID)
        {
            if(AS.GetAssignmentByID(AssignmentID) == null)
            {
                throw new Exception();
            }
            if (CourseID != null)
            {
                if (!AS.CourseExist(CourseID))
                {
                    throw new Exception();
                }
            }
            var ViewModel = new MilestoneViewModel();
            ViewModel.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), CourseID);
            return View(ViewModel);
        }

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult EditAssignment(int AssignmentID)
        {
            var Assignment = AS.GetAssignmentByID(AssignmentID);
            Assignment.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), Assignment.CourseID);
            Assignment.UserDataLinks = TS.GetAssignmentLinks(Assignment);
            return View(Assignment);
        }

        public ActionResult RemoveFile(string FilePath)
        {
            TS.DeleteAssignmentFile(FilePath);
            return Redirect(Request.UrlReferrer.ToString());
        }

        [HttpPost]
        [Authorize(Roles = "Teachers")]
        public ActionResult EditAssignment(AssignmentViewModel model)
        {
            if (ModelState.IsValid)
            {
                ModelState.Clear();
                TS.EditAssignment(model);
                return RedirectToAction("StudentAssignments", "User", new { id = model.ID });
            }
            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
            return View(model);
        }


        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult EditMilestone(int MilestoneID)
        {
            var Milestone = AS.GetMilestoneByID(MilestoneID);
            Milestone.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), Milestone.CourseID);
            return View(Milestone);
        }
        /// <summary>
        /// Teacher edits current milestone for assignment
        /// sends in .zip with the program (main.cpp) and .txt with input if there is any.
        /// gets in return values from the compiler.
        /// </summary>
        [HttpPost]
        [Authorize(Roles = "Teachers")]
        public ActionResult EditMilestone(MilestoneViewModel model, HttpPostedFileBase ZipFile, HttpPostedFileBase TxtFile)
        {
            if (ModelState.IsValid)
            {
                ModelState.Clear();
                if (ZipFile != null)
                {
                    var ZipType = "zip";
                    var TextType = "txt";

                    var ZipEnding = System.IO.Path.GetExtension(ZipFile.FileName).Substring(1);
                    if (!ZipType.Contains(ZipEnding))
                    {
                        ViewBag.Output = "Error: upload approriate .zip file";
                        model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
                        return View(model);
                    }
                    if(TxtFile != null)
                    {
                        var TextEnding = System.IO.Path.GetExtension(TxtFile.FileName).Substring(1);
                        if (!TextType.Contains(TextEnding))
                        {
                            ViewBag.Output = "Error: upload approriate .txt file";
                            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
                            return View(model);
                        }
                    }
                    Stopwatch watch = new Stopwatch();
                    watch.Start();

                    try
                    {
                        model = TS.CompileMilestoneUpload(model, ZipFile, TxtFile);
                    }
                    catch
                    {
                        //return error, compile failed, invalid file?
                        throw new Exception();
                    }

                    watch.Stop();
                    TimeSpan ts = watch.Elapsed;
                    ViewBag.Output = "Compiled in " + ts.Seconds + "." + ts.Milliseconds / 10 + " seconds";
                }
                TS.EditMilestone(model);
            }
            model.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);
            return View(model);
        }

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult DeleteAssignment(int AssID, int? CourseID)
        {
            TS.DeleteAssignment(AssID);
            return RedirectToAction("TeacherHome", "User", new { id = CourseID });
        }

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult DeleteMilestone(int MileID, int CourseID)
        {
            TS.DeleteMilestone(MileID);
            return RedirectToAction("TeacherHome", "User", new { id = CourseID });
        }
        /// <summary>
        /// Student sends in a solution to a milestone
        /// This function contancts studentcompile which uses the compiler
        /// gets in return status for the submission if it failed or succeeded.
        /// </summary>
        [HttpPost]
        public ActionResult StudentSubmit(MilestoneViewModel model, HttpPostedFileBase ZipFile)
        {
            if(ZipFile != null)
            {
                var ZipType = "zip";
                var ZipEnding = System.IO.Path.GetExtension(ZipFile.FileName).Substring(1);
                if (!ZipType.Contains(ZipEnding))
                {
                    return RedirectToAction("StudentMilestones", "User", new { id = model.ID, SubID = model.SubmissionID });
                }
                SubmissionViewModel submission = new SubmissionViewModel();

                try
                {
                    // compiler called
                    submission = US.StudentCompile(model, ZipFile);
                }
                catch
                {
                    // return error, compile failed, invalid file?
                    throw new Exception();
                }
                submission.Grade = Math.Round(LS.CalculateSimilarity(submission.Output, model.Output) * 10, 2);

                submission.Status = false;
                if(submission.Output == model.Output)
                {
                    submission.Status = true;
                }
                // checks for dr.memory error
                if (!submission.DrMemory.Contains("NO ERRORS FOUND:"))
                {
                    submission.Grade = submission.Grade - 1;
                    submission.Status = false;
                }
                SS.AddSubmission(submission);

                var ViewModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), model.CourseID);

                if (ViewModel.Submissions != null)
                {
                    foreach (var m in ViewModel.Submissions)
                    {
                        m.AssignmentName = AS.GetAssignmentByID(m.AssignmentID).Name;
                    }
                }

                // auto grading system, checks which submission is the best.
                if (ViewModel.Assignments != null)
                {
                    foreach (var ass in ViewModel.Assignments)
                    {
                        var submissions = ViewModel.Submissions.Where(x => x.AssignmentID == ass.ID).ToList();
                        ass.Grade = AS.GetGradeForAssignment(ass.Milestones, submissions);
                    }
                }
            }
            
            return RedirectToAction("StudentMilestones", "User", new { id = model.ID, SubID = model.SubmissionID });
        }
    }
}