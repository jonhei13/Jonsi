using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Mooshak2._0.Services;
using Microsoft.AspNet.Identity;
using Mooshak2._0.Models.ViewModels;

namespace Mooshak2._0.Controllers
{
    public class UserController : Controller
    {
        private UserService US = new UserService(null);
        private AssignmentService AS = new AssignmentService(null);
        private SubmissionService SS = new SubmissionService(null);
        private TeacherService TS = new TeacherService();

        [Authorize(Roles = "Students, Teachers")]
        public ActionResult StudentHome(int? id)
        {
            var ViewModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), id);

            if(ViewModel.Submissions != null)
            {
                foreach (var m in ViewModel.Submissions)
                {
                    m.AssignmentName = AS.GetAssignmentByID(m.AssignmentID).Name;
                }
            }

            if(ViewModel.Assignments != null)
            {
                foreach (var ass in ViewModel.Assignments)
                {
                    var submissions = ViewModel.Submissions.Where(x => x.AssignmentID == ass.ID).ToList();
                    ass.Grade = AS.GetGradeForAssignment(ass.Milestones, submissions);
                }
            }

            return View(ViewModel);
        }

        [Authorize(Roles = "Students, Teachers")]
        public ActionResult StudentAssignments(int id)
        {
            var AssignmentViewModel = AS.GetAssignmentByID(id);
            if(AssignmentViewModel == null)
            {
                throw new Exception();
            }
            AssignmentViewModel.UserDataLinks = TS.GetAssignmentLinks(AssignmentViewModel);
            AssignmentViewModel.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), AssignmentViewModel.CourseID);
            AssignmentViewModel.UserModel.AssignmentID = id;
            return View(AssignmentViewModel);
        }
        /// <summary>
        /// Returns all student milestones for submission
        /// </summary>
        [Authorize(Roles = "Students, Teachers")]
        public ActionResult StudentMilestones(int id, int? SubID)
        {
            var MilestoneViewModel = AS.GetMilestoneByID(id);
            if(MilestoneViewModel == null)
            {
                throw new Exception();
            }
            var AssignmentViewModel = AS.GetAssignmentByID(MilestoneViewModel.AssignmentID);
            MilestoneViewModel.UserDataLinks = TS.GetMilestoneLinks(MilestoneViewModel, User.Identity.GetUserName());
            MilestoneViewModel.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), AssignmentViewModel.CourseID);
            MilestoneViewModel.Users = TS.GetAllStudentsInCourse(AssignmentViewModel.CourseID);
            MilestoneViewModel.Submissions = TS.GetSubmissionsInMilestone(MilestoneViewModel.ID);

            if(SubID == null)
            {
                try
                {
                    MilestoneViewModel.SubmissionID = MilestoneViewModel.UserModel.Submissions.Where(x => x.MilestoneID == id).FirstOrDefault().ID;
                }
                catch { }
            }
            else
            {
                MilestoneViewModel.SubmissionID = SubID;
            }
            MilestoneViewModel.UserModel.AssignmentID = MilestoneViewModel.AssignmentID;
            return View(MilestoneViewModel);
        }

        [Authorize(Roles = "Teachers")]
        public ActionResult TeacherHome(int? id)
        {
            var ViewModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), id);

            return View(ViewModel);
        }

        [HttpPost]
        [Authorize(Roles = "Teachers")]
        public ActionResult TeacherComment(SubmissionViewModel sub)
        {
            if(!ModelState.IsValid)
            {
                sub.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), sub.CourseID);
                return View(sub);
            }
            TS.TeacherComment(sub.Comment, sub.ID, sub.Grade);
            return RedirectToAction("StudentMilestones", "User", new { id = sub.MilestoneID });
        }

        [HttpGet]
        [Authorize(Roles = "Teachers")]
        public ActionResult TeacherComment(int subID)
        {
            var sub = SS.GetSubmissionByID(subID);
            sub.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), sub.CourseID);
            return View(sub);
        }
    }
}