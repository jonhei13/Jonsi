﻿using Mooshak2._0.Models;
using System.Web;
using System.Web.Mvc;

namespace Mooshak2._0
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
            //filters.Add(new CustomHandleErrorAttribute());
        }
    }
}
