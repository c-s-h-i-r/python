import calendar
import datetime




'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# def getSundays():
	# startDate = datetime.date(1901,1,1)
	# endDate = datetime.date(2000,1,1)
    # count = 0
    # while (startDate < endDate):
        # if (startDate.day == 1 && startDate.today.weekday == 6):
            # count++
        # startDate
    # return count
    
# print getSundays()

from datetime import timedelta

def subtract_one_month(dt0):
    dt1 = dt0.replace(days=+1)
    dt2 = dt1 - timedelta(days=+1)
    dt3 = dt2.replace(days=+1)
    return dt3
a = datetime.date(2004,3,30)
subtract_one_month(a)
print a