using Microsoft.VisualStudio.TestTools.UnitTesting;
using Mooshak2._0.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mooshak2._0.test;
using Mooshak2._0.Models.Entities;

namespace Mooshak2._0.Services.Tests
{
    [TestClass]
    public class SubmissionServiceTests
    {
        private SubmissionService _SS;

        [TestInitialize]
        public void Initialize()
        {

            // Set up our mock database.
            var MockDb = new MockDataContext();
            var User1 = new UserCourse
            {
                ID = 1,
                UserName = "Arnar",
                CourseID = 1
            };
            MockDb.UserCourse.Add(User1);

            var User2 = new UserCourse
            {
                ID = 2,
                UserName = "Alex",
                CourseID = 1
            };
            MockDb.UserCourse.Add(User2);

            var Course1 = new Course
            {
                ID = 1,
                Name = "Course1"
            };
            MockDb.Course.Add(Course1);

            var Ass1 = new Assignment
            {
                ID = 1,
                Name = "Assignment1",
                CourseID = 1
            };
            MockDb.Assignment.Add(Ass1);

            var Mile1 = new Milestone
            {
                ID = 1,
                Name = "Milestone1",
                AssignmentID = 1
            };
            MockDb.Milestone.Add(Mile1);

            var Sub1 = new Submission
            {
                ID = 1,
                UserName = "Arnar",
                MilestoneID = 1,
                AssignmentID = 1,
                CourseID = 1
            };
            MockDb.Submission.Add(Sub1);

            _SS = new SubmissionService(MockDb);
        }
        [TestMethod]
        public void GetUserSubmissionsByCourseIDTest()
        {
            string Username = "Arnar";
            int CourseID = 1;

            var Submissions = _SS.GetUserSubmissionsByCourseID(Username, CourseID);

            Assert.AreEqual(1, Submissions.Count);
        }

        [TestMethod]
        public void GetSubmissionByIdMilestoneIDTest()
        {
            int MileID = 1;

            var SubByMileID = _SS.GetSubmissionByIdMilestoneID(MileID);

            Assert.AreEqual(1, SubByMileID.AssignmentID);
        }

        [TestMethod]
        public void GetSubmissionByIDTest()
        {
            int SubID = 1;

            var TheSub = _SS.GetSubmissionByID(SubID);

            Assert.AreEqual(1, TheSub.CourseID);
        }
    }
}