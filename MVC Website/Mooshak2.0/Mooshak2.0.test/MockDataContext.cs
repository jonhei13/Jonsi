using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mooshak2._0.Models;
using Mooshak2._0.Models.Entities;
using System.Data.Entity;

namespace Mooshak2._0.test
{
    class MockDataContext : IAppDataContext
    {
        public MockDataContext()
        {
            Submission = new InMemoryDbSet<Submission>();
            Milestone = new InMemoryDbSet<Milestone>();
            UserCourse = new InMemoryDbSet<UserCourse>();
            Course = new InMemoryDbSet<Course>();
            Assignment = new InMemoryDbSet<Assignment>();
        }

        public IDbSet<Milestone> Milestone { get; set; }
        public IDbSet<UserCourse> UserCourse { get; set; }
        public IDbSet<Course> Course { get; set; }
        public IDbSet<Assignment> Assignment { get; set; }
        public IDbSet<Submission> Submission { get; set; }

        public int SaveChanges()
        {
            int Changes = 0;
            return Changes;
        }

        public void Dispose()
        {
            //Do nothing
        }
    }
}
