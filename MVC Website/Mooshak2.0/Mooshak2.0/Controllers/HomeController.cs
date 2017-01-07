using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Mooshak2._0.Services;
using Microsoft.AspNet.Identity;

namespace Mooshak2._0.Controllers
{
    public class HomeController : Controller
    {
        [Authorize]
        public ActionResult Index()
        {
            IdentityManager IM = new IdentityManager();
            if(IM.UserIsInRole(User.Identity.GetUserId(), "Administrators"))
            {   
                return RedirectToAction("AdminHome", "Admin", new { username = User.Identity.GetUserName() });
            }
            else if(IM.UserIsInRole(User.Identity.GetUserId(), "Students"))
            {
                return RedirectToAction("StudentHome", "User", new { username = User.Identity.GetUserName() });
            }
            else if (IM.UserIsInRole(User.Identity.GetUserId(), "Teachers"))
            {
                return RedirectToAction("TeacherHome", "User", new { username = User.Identity.GetUserName() });
            }
            return View();
        }
    }
}