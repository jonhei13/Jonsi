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
    public class AssignmentService
    {
        private SubmissionService sub = new SubmissionService(null);
        private CompilerService _cp = new CompilerService();
        private SubmissionService SS = new SubmissionService(null);
        private readonly IAppDataContext _db;

        public AssignmentService(IAppDataContext dbContext)
        {
            _db = dbContext ?? new ApplicationDbContext();
        }

        /// <summary>
        /// Get a single assignment from the database
        /// and every milestone it has.
        /// </summary>
        public AssignmentViewModel GetAssignmentByID(int AssignmentID)
        {
            var assignment = _db.Assignment.SingleOrDefault(x => x.ID == AssignmentID);
            if (assignment == null)
            {
                return null;
            }

            // After the assignment is found, we find all the milestones belonging to it.
            var ListMilestones = _db.Milestone
                .Where(x => x.AssignmentID == AssignmentID)
                .Select(x => new MilestoneViewModel
                {
                    ID = x.ID,
                    AssignmentID = x.AssignmentID,
                    CourseID = x.CourseID,
                    Name = x.Name,
                    Description = x.Description,
                    Input = x.Input,
                    Output = x.Output,
                    Percent = x.Percent
                })
                .ToList();

            // After all the milestones have been retrieved, we create the assignment
            // and finally return it.
            var ViewModel = new AssignmentViewModel
            {
                ID = assignment.ID,
                CourseID = assignment.CourseID,
                Hidden = assignment.Hidden,
                Name = assignment.Name,
                DueDate = assignment.DueDate,
                StartDate = assignment.StartDate,
                FilePath = assignment.FilePath,
                Milestones = ListMilestones
            };
            return ViewModel;
        }

        /// <summary>
        /// Get all assignments in a specific course.
        /// </summary>
        public List<AssignmentViewModel> GetAssignmentsByCourseID(int? CourseID)
        {
            if (CourseID == null)
            {
                return null;
            }

            // First we retrive all the assignments
            var AssignmentsID = _db.Assignment
                .Where(x => x.CourseID == CourseID)
                .Select(x => new
                {
                    ID = x.ID,
                }
                ).ToList();

            if (AssignmentsID == null)
            {
                return null;
            }

            // Then if something is found we add it to a list, and finally return it.
            List<AssignmentViewModel> Assignments = new List<AssignmentViewModel>();

            foreach (var Ass in AssignmentsID)
            {
                Assignments.Add(GetAssignmentByID(Ass.ID));
            }

            return Assignments;
        }

        /// <summary>
        /// Get a single milestone from the database.
        /// </summary>
        public MilestoneViewModel GetMilestoneByID(int MileID)
        {
            var Milestone = _db.Milestone.SingleOrDefault(x => x.ID == MileID);
            if (Milestone == null)
            {
                return null;
            }
            var ViewModel = new MilestoneViewModel
            {
                ID = Milestone.ID,
                AssignmentID = Milestone.AssignmentID,
                CourseID = Milestone.CourseID,
                Name = Milestone.Name,
                Description = Milestone.Description,
                Input = Milestone.Input,
                Output = Milestone.Output,
                Percent = Milestone.Percent
            };
            return ViewModel;
        }

        /// <summary>
        ///  Rather complicated function.
        ///  
        ///  in short: finds the submission with the highest grade for every milestone, and returns the 
        ///  grade for a single assignment, this function is part of the auto grading system.
        ///  
        ///  1. Takes in list of milestones and submissions
        ///  2. Loops trough all milestones
        ///  3. While looping trough all milestones, it also loops through all submissions
        ///  4. Compares the milestoneID to the submission, and if the submission belongs to a specific milestone
        ///     then it checks if the grade is higher than previous highest
        ///  5. After all the loops have finished, then we mark the best graded assignemnt for the teacher to see
        ///  6. Finally after all the data manipulation, we can finally calculate the grade for the assignment.
        /// </summary>
        public double GetGradeForAssignment(List<MilestoneViewModel> Mile, List<SubmissionViewModel> Submission)
        {
            double TheGrade = 0;
            SubmissionViewModel Highest = new SubmissionViewModel();
            List<double> grades = new List<double>();
            List<SubmissionViewModel> subs = new List<SubmissionViewModel>();

            try
            {
                foreach (var m in Mile)
                {
                    SubmissionViewModel TheSub = new SubmissionViewModel();
                    TheSub.Grade = 0;
                    foreach (var s in Submission)
                    {
                        // here we compare if the submission belongs to the milestone.
                        // and if the grade is higher than previous found grade.
                        if (s.Grade >= TheSub.Grade && s.MilestoneID == m.ID)
                        {
                            TheSub = s;
                            Highest = s;
                        }
                    }
                    // after we loop trough single milestone we add a single
                    // submission with the highest grade to a list.
                    subs.Add(TheSub);
                    // Mark a single submit that has the highest grade.
                    SS.ToSubmit(Highest);
                }
                // and calculated the grade for the assignment and finally return it.
                foreach (var sub in subs)
                {
                    TheGrade += sub.Grade*Mile.SingleOrDefault(x => x.ID == sub.MilestoneID).Percent;
                }
            }
            catch
            {
            }
            TheGrade = Math.Round((TheGrade/100), 2);
            return TheGrade;
        }

        /// <summary>
        /// Checks if a specific course exists in the database
        /// </summary>
        public bool CourseExist(int? CourseID)
        {
            if (CourseID == null)
            {
                return true;
            }
            // we have to check if the courseID is null before, because it is nullable int.
            var Course = _db.Course.SingleOrDefault(x => x.ID == CourseID);
            if (Course == null)
            {
                return false;
            }
            return true;
        }
    }
}