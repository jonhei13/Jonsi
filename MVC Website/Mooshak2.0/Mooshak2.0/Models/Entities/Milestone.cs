using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.Entities
{
    public class Milestone
    {

        public int ID { get; set; }
        public int AssignmentID { get; set; }
        public int CourseID { get; set; }
        public double Percent { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public string Output { get; set; }
        public string Input { get; set; }

    }
}