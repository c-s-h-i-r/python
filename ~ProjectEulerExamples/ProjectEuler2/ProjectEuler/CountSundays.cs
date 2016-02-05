using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    /// <summary>
    /// 1 Jan 1900 was a Monday.
    /// Thirty days has September,
    /// April, June and November.
    /// All the rest have thirty-one,
    /// Saving February alone,
    /// Which has twenty-eight, rain or shine.
    /// And on leap years, twenty-nine.
    /// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    /// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?    
    /// </summary>
    class CountSundays
    {
        private DateTime endDate = new DateTime(2000, 12, 31);
        private DateTime startDate = new DateTime(1901, 01, 1);

        private IDictionary<string, int> daysinMonth = new Dictionary<string, int>(){
                                                         {"January",31},
                                                         {"February",28},
                                                         { "March",31},
                                                         {"April",30},
                                                         {"May",31},
                                                         {"June",30},
                                                         {"July",31},
                                                         {"August",31},
                                                         {"September",30},
                                                         {"October",31},
                                                         {"November", 30},
                                                         {"December", 31}
                                                        };
        private int count = 0;
        public int getCount()
        {
            while (-1 == startDate.CompareTo(endDate))
            {
                if (startDate.Date.Day == 1 && startDate.Date.DayOfWeek.Equals(DayOfWeek.Sunday))
                {
                    count++;
                }
                startDate = startDate.AddMonths(1);
            }
            return count;
        }

        //ctr
        public CountSundays()
        {
            Console.WriteLine(this.getCount());
        }

        
    }
}
