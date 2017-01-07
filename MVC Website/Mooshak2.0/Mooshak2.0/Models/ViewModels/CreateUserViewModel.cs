using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Mooshak2._0.Models.ViewModels
{
    public class CreateUserViewModel
    {
        [Required]
        public string Role { get; set; }
        [EmailAddress]
        public string Username { get; set; }
        public string Password { get; set; }
        public List<SelectListItem> Courses { get; set; }
        public int CourseID { get; set; }
        public string Email { get; set; }

    }
}