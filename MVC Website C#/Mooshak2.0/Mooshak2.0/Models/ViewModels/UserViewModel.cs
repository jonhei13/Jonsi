using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Mooshak2._0.Models.ViewModels
{
    public class UserViewModel
    {

        public string ID { get; set; }
        [Required]
        public string UserName { get; set; }
        public string Role { get; set; }
        public int CourseId { get; set; }
        public bool IsSelected { get; set; }
        public List<CourseViewModel> Courses { get; set; }
        public List<SelectListItem> CourseList { get; set; }



    }
}