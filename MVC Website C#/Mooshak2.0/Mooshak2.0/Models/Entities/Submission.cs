using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.Entities
{
    public class Submission
    {

        public int ID{ get; set; }
        public string UserName { get; set; }
        public int MilestoneID { get; set; }
        public int AssignmentID { get; set; }
        public int CourseID { get; set; }
        public double Grade { get; set; }
        public string Output { get; set; }
        public string Error { get; set; }
        public string FilePath { get; set; }
        public string DrMemory { get; set; }
        public bool Status { get; set; }
        public bool ToSubmit { get; set; }
        public string Comment { get; set; }

    }
}