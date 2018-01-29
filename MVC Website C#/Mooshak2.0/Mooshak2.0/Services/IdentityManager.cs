using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.EntityFramework;
using Mooshak2._0.Models;
using Mooshak2._0.Models.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;


using System.Web.Mvc;
using System.Web.Optimization;
using System.Web.Routing;

namespace Mooshak2._0.Services
{
    /// <summary>
    /// Identity manager is class with multiple functions to help out with
    /// the intigrated identity system in MVC
    /// this file was implemented into the project as a whole, and was not created by
    /// us.
    /// </summary>
    public class IdentityManager
    {
        private ApplicationDbContext _db = new ApplicationDbContext();

        public static void init()
        {
            /*
            IdentityManager manager = new IdentityManager();

            if (!manager.RoleExists("Administrators"))
            {
                manager.CreateRole("Administrators");
            }

            if(!manager.RoleExists("Teachers"))
            {
                manager.CreateRole("Teachers");
            }

            if (!manager.RoleExists("Students"))
            {
                manager.CreateRole("Students");
            }

            if (!manager.UserExists("admin@admin.is"))
            {
                ApplicationUser newAdmin = new ApplicationUser();
                newAdmin.UserName = "admin@admin.is";
                manager.CreateUser(newAdmin, "123456");
                manager.AddUserToRole(newAdmin.Id, "Administrators");
            }

            if (!manager.UserExists("student@student.is"))
            {
                ApplicationUser newAdmin = new ApplicationUser();
                newAdmin.UserName = "student@student.is";
                manager.CreateUser(newAdmin, "123456");
                manager.AddUserToRole(newAdmin.Id, "Students");
            }

            if (!manager.UserExists("teacher@teacher.is"))
            {
                ApplicationUser newAdmin = new ApplicationUser();
                newAdmin.UserName = "teacher@teacher.is";
                manager.CreateUser(newAdmin, "123456");
                manager.AddUserToRole(newAdmin.Id, "Teachers");
            }
            */

        }
        public bool RoleExists(string name)
        {
            var rm = new RoleManager<IdentityRole>(new RoleStore<IdentityRole>(new ApplicationDbContext()));
            return rm.RoleExists(name);
        }

        public bool CreateRole(string name)
        {
            var rm = new RoleManager<IdentityRole>(new RoleStore<IdentityRole>(new ApplicationDbContext()));
            var idResult = rm.Create(new IdentityRole(name));
            return idResult.Succeeded;
        }

        public bool UserExists(string name)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            return um.FindByName(name) != null;
        }

        public ApplicationUser GetUser(string name)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            return um.FindByName(name);
        }

        public bool CreateUser(ApplicationUser user, string password)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var idResult = um.Create(user, password);
            return idResult.Succeeded;
        }

        public bool AddUserToRole(string userId, string roleName)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var idResult = um.AddToRole(userId, roleName);
            return idResult.Succeeded;
        }

        public bool UserIsInRole(string userId, string roleName)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var result = um.IsInRole(userId, roleName);
            return result;
        }

        public void ClearUserRoles(string userId)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var rm = new RoleManager<IdentityRole>(new RoleStore<IdentityRole>(new ApplicationDbContext()));
            var user = um.FindById(userId);
            var currentRoles = new List<IdentityUserRole>();
            currentRoles.AddRange(user.Roles);
            foreach (var role in currentRoles)
            {
                var r = rm.FindById(role.RoleId);
                um.RemoveFromRole(userId, r.Name);
            }
        }

        public string GetUserRole(string userId)
        {
            var Role = GetUserRoles(userId);
            if(Role.Count == 0)
            {
                return null;
            }
            return Role.First();
        }
        public IList<string> GetUserRoles(string userId)
        {
            var um = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var result = um.GetRoles(userId);
            return result;
        }
        public void ChangePassword(string userId, string password)
        {
            var ManageUser = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            ManageUser.RemovePassword(userId);
            ManageUser.AddPassword(userId, password);
        }

        public void DeleteUser(string UserId)
        {
            var ManageUser = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var Users = ManageUser.FindById(UserId);
            ManageUser.Delete(Users);
        }
        public UserViewModel GetEditedUser(string UserId)
        {
            var Users = new UserViewModel();
            var ManageUser = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var OldUser = ManageUser.FindById(UserId);
            if(OldUser != null)
            {
                Users.UserName = OldUser.UserName;
                Users.ID = OldUser.Id;
            }
            return Users;
        }
        public void EditUser(UserViewModel model)
        { 
            var ManageUser = new UserManager<ApplicationUser>(new UserStore<ApplicationUser>(new ApplicationDbContext()));
            var User = ManageUser.FindById(model.ID);
            var TheUser = _db.Users.SingleOrDefault(x => x.UserName == User.UserName);
            TheUser.UserName = model.UserName;
            _db.SaveChanges();
        }
    }
}