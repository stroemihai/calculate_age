import time
from calendar import isleap

# check if the year is leap or not
def check_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("input your name: ")
age = input("input your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for i in range(begin_year, end_year):
    if check_leap_year(i):
        day = day + 366
    else:
        day = day + 365

leap_year = check_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
