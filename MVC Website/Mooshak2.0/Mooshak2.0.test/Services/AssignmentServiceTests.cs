using Microsoft.VisualStudio.TestTools.UnitTesting;
using Mooshak2._0.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mooshak2._0.Models;
using Mooshak2._0.test;
using Mooshak2._0.Models.Entities;


namespace Mooshak2._0.Services.Tests
{
    [TestClass]
    public class AssignmentServiceTests
    {
        private AssignmentService _AS;

        [TestInitialize]
        public void Initialize()
        {
            // Set up our mock database.
            var MockDb = new MockDataContext();
            var Ass1 = new Assignment
            {
                ID = 1,
                Name = "Assignment1",
                CourseID = 1
            };
            MockDb.Assignment.Add(Ass1);

            var Ass2 = new Assignment
            {
                ID = 2,
                Name = "Assignment2",
                CourseID = 1
            };
            MockDb.Assignment.Add(Ass2);

            var Cour1 = new Course
            {
                ID = 1,
                Name = "Course1"
            };
            MockDb.Course.Add(Cour1);

            var Mile1 = new Milestone
            {
                ID = 1,
                Name = "Milestone1"
            };
            MockDb.Milestone.Add(Mile1);

            var Mile2 = new Milestone
            {
                ID = 2,
                Name = "Milestone2"
            };
            MockDb.Milestone.Add(Mile2);

            var Mile3 = new Milestone
            {
                ID = 3,
                Name = "Milestone3"

            };
            MockDb.Milestone.Add(Mile3);
       
            _AS = new AssignmentService(MockDb);
        }

        [TestMethod]
        public void GetMilestoneByIDTest()
        {
            int ID = 1;

            var TheMilestone = _AS.GetMilestoneByID(ID);

            Assert.IsTrue("Milestone1" == TheMilestone.Name);
        }

        [TestMethod]
        public void GetAssignmentByIDTest()
        {
            int ID = 1;

            var TheAssignment = _AS.GetAssignmentByID(ID);

            Assert.IsTrue("Assignment1" == TheAssignment.Name);
        }

        [TestMethod]
        public void CourseExistTest()
        {
            int CourseID = 1;

            var TheCourse = _AS.CourseExist(CourseID);

            Assert.IsTrue(TheCourse);
        }

        [TestMethod]
        public void GetAssignmentsByCourseIDTest()
        {
            int CourseID = 1;

            var TheAssignments = _AS.GetAssignmentsByCourseID(CourseID);

            Assert.AreEqual(2, TheAssignments.Count);
        }
    }
}