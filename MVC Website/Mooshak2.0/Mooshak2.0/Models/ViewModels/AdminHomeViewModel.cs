using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class AdminHomeViewModel
    {
        public int CourseID { get; set; }
        public string CourseName { get; set; }
        public string UserID { get; set; }
        public List<CourseViewModel> Courses { get; set; }
        public List<UserViewModel> Users { get; set; }

    }
}