﻿using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Mooshak2._0.Models.ViewModels
{
    public class CourseViewModel
    {

        public int ID { get; set; }
        [Required]
        public string Name { get; set; }
        public List<UserViewModel> Users { get; set; }
        public bool IsSelected { get; set; }


    }
}