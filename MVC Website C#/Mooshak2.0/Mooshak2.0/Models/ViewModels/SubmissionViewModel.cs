using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class SubmissionViewModel
    {

        public int ID { get; set; }
        public string UserName { get; set; }
        public int AssignmentID { get; set; }
        public int MilestoneID { get; set; }
        public int CourseID { get; set; }
        public string AssignmentName { get; set; }
        public string Input { get; set; }
        public string Output { get; set; }
        public string Error { get; set; }
        public string DrMemory { get; set; }
        public string FilePath { get; set; }
        [Required]
        [Range(typeof(double), "0", "10", ErrorMessage = "{0} can only be between {1} and {2}")]
        public double Grade { get; set; }
        public bool Status { get; set; }
        public bool ToSubmit { get; set; }
        [Required]
        public string Comment { get; set; }
        public UserHomeViewModel UserModel { get; set; }

    }
}