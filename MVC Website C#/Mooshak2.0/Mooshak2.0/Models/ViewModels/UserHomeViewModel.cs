using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class UserHomeViewModel
    {
        public string Name { get; set; }
        public string UserID { get; set; }
        public int? CourseID { get; set; }
        public string CourseName { get; set; }
        public int AssignmentID { get; set; }
        public List<CourseViewModel> Courses { get; set; }
        public List<AssignmentViewModel> Assignments { get; set; }
        public List<SubmissionViewModel> Submissions { get; set; }

    }
}