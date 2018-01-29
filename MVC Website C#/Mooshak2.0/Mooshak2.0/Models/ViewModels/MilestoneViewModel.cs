using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class MilestoneViewModel
    {

        public int ID { get; set; }
        public int AssignmentID { get; set; }
        public int CourseID { get; set; }
        public int? SubmissionID { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public string Description { get; set; }
        public string Input { get; set; }
        public string Output { get; set; }
        public string DrMemory { get; set; }
        public double Percent { get; set; } 
        public List<string> UserDataLinks { get; set; }
        public UserHomeViewModel UserModel { get; set; }
        public List<SubmissionViewModel> Submissions { get; set; }
        public List<UserViewModel> Users { get; set; }

    }
}