using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.Entities
{
    public class Assignment
    {

        public int ID { get; set; }
        public int CourseID { get; set; }
        public string Name { get; set; }
        public string FilePath { get; set; }
        public bool Hidden { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime DueDate { get; set; }

    }
}