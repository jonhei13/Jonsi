using Mooshak2._0.Models.ViewModels;
using Mooshak2._0.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using Microsoft.AspNet.Identity;

namespace Mooshak2._0.Controllers
{
    public class ErrorController : Controller
    {
        UserService US = new UserService(null);

        public ActionResult AccessDenied()
        {
            Response.StatusCode = (int)HttpStatusCode.Forbidden;
            Response.TrySkipIisCustomErrors = true;

            if(!User.Identity.IsAuthenticated)
            {
                return View();
            }

            MilestoneViewModel theview = new MilestoneViewModel();
            theview.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), null);

            return View(theview);
        }

        public ActionResult NotFound()
        {
            Response.StatusCode = (int)HttpStatusCode.NotFound;
            Response.TrySkipIisCustomErrors = true;

            if (!User.Identity.IsAuthenticated)
            {
                return View();
            }

            MilestoneViewModel theview = new MilestoneViewModel();
            theview.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), null);

            return View(theview);
        }

        public ActionResult ApplicationError()
        {
            Response.StatusCode = (int)HttpStatusCode.InternalServerError;
            Response.TrySkipIisCustomErrors = true;

            if (!User.Identity.IsAuthenticated)
            {
                return View();
            }

            MilestoneViewModel theview = new MilestoneViewModel();
            theview.UserModel = US.GetUserOverviewByUserName(User.Identity.GetUserName(), null);

            return View(theview);
        }
    }
}