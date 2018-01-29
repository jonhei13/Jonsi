using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class AssignmentViewModel
    {

        public int ID { get; set; }
        [Required]
        public int CourseID { get; set; }
        [Required]
        public bool Hidden { get; set; }
        [Required]
        public String Name { get; set; }
        [Required]
        [DataType(DataType.DateTime)]
        [Range(typeof(DateTime), "1/1/2000", "1/1/2050")]
        public DateTime DueDate { get; set; }
        [Required]
        [DataType(DataType.DateTime)]
        [Range(typeof(DateTime), "1/1/2000", "1/1/2050")]
        public DateTime StartDate { get; set; }
        public string FilePath { get; set; }
        public double Grade { get; set; }
        public List<MilestoneViewModel> Milestones { get; set; }
        public UserHomeViewModel UserModel { get; set; }
        public List<string> UserDataLinks { get; set; }

    }
}