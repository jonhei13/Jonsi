using Mooshak2._0.Models;
using Mooshak2._0.Models.Entities;
using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Services
{
    public class SubmissionService
    {
        private readonly IAppDataContext _db;

        public SubmissionService(IAppDataContext dbContext)
        {
            _db = dbContext ?? new ApplicationDbContext();
        }
        /// <summary>
        /// Get all submissions, for all assignments and every milestone, in a specific course for a 
        /// specific user.
        /// </summary>
        public List<SubmissionViewModel> GetUserSubmissionsByCourseID(string User, int? CourseID)
        {
            if(CourseID == null)
            {
                return null;
            }

            var Submissions = _db.Submission
                .Where(x => x.CourseID == CourseID && x.UserName == User)
                .Select(x => new SubmissionViewModel
                {
                    ID = x.ID,
                    MilestoneID = x.MilestoneID,
                    UserName = x.UserName,
                    AssignmentID = x.AssignmentID,
                    Output = x.Output,
                    Error = x.Error,
                    FilePath = x.FilePath,
                    Grade = x.Grade,
                    Status = x.Status,
                    DrMemory = x.DrMemory,
                    ToSubmit = x.ToSubmit,
                    Comment = x.Comment
                })
                .ToList();

            return Submissions;
        }
        /// <summary>
        /// Returns all submissions from all users for a specific milestone.
        /// </summary>
        public SubmissionViewModel GetSubmissionByIdMilestoneID(int MileID)
        {
            var submission = _db.Submission.SingleOrDefault(x => x.MilestoneID == MileID);
            if (submission == null)
            {
                return null;
            }

            var ViewModel = new SubmissionViewModel
            {
                UserName = submission.UserName,
                AssignmentID = submission.AssignmentID,
                MilestoneID = submission.MilestoneID,
                Output = submission.Output,
                Error = submission.Error,
                FilePath = submission.FilePath,
                Grade = submission.Grade,
                Status = submission.Status,
                DrMemory = submission.DrMemory,
                ToSubmit = submission.ToSubmit,
                Comment = submission.Comment
            };
            return ViewModel;
        }
        /// <summary>
        /// Adds a submission to the database from a student.
        /// </summary>
        public void AddSubmission(SubmissionViewModel sub)
        {
            if(sub == null)
            {
                return;
            }

            Submission NewSub = new Submission();

            NewSub.AssignmentID = sub.AssignmentID;
            NewSub.CourseID = sub.CourseID;
            NewSub.Error = sub.Error;
            NewSub.FilePath = sub.FilePath;
            NewSub.Grade = sub.Grade;
            NewSub.MilestoneID = sub.MilestoneID;
            NewSub.Output = sub.Output;
            NewSub.Status = sub.Status;
            NewSub.UserName = sub.UserName;
            NewSub.DrMemory = sub.DrMemory;
            NewSub.Comment = sub.Comment;

            _db.Submission.Add(NewSub);
            _db.SaveChanges();
        }
        /// <summary>
        /// Function for the automated grading system.
        /// It takes in a single submission that has the highest grade
        /// and flags to be submitted.
        /// While doing so, it marks all other submissions in the database for
        /// that specific milestone to false, so the previous submissions (if there were any)
        /// that were marked for submission, will be unmarked. 
        /// </summary>
        public void ToSubmit(SubmissionViewModel TheSub)
        {
            var Submissions = _db.Submission.Where(x => x.MilestoneID == TheSub.MilestoneID && x.UserName == TheSub.UserName).ToList();

            if(Submissions == null)
            {
                return;
            }
            // here we flag all submission to false, except the one with the highest grade.
            foreach(var sub in Submissions)
            {
                sub.ToSubmit = false;
                if(sub.ID == TheSub.ID)
                {
                    sub.ToSubmit = true;
                }
            }

            _db.SaveChanges();
        }
        /// <summary>
        /// Returns a single submission from the database by its ID
        /// </summary>
        public SubmissionViewModel GetSubmissionByID(int SubID)
        {
            var submission = _db.Submission.SingleOrDefault(x => x.ID == SubID);

            if(submission == null)
            {
                throw new Exception();
            }

            var ViewModel = new SubmissionViewModel
            {
                ID = submission.ID,
                UserName = submission.UserName,
                AssignmentID = submission.AssignmentID,
                MilestoneID = submission.MilestoneID,
                Output = submission.Output,
                Error = submission.Error,
                FilePath = submission.FilePath,
                Grade = submission.Grade,
                Status = submission.Status,
                DrMemory = submission.DrMemory,
                ToSubmit = submission.ToSubmit,
                Comment = submission.Comment,
                CourseID = submission.CourseID
            };

            return ViewModel;
        }
    }
}