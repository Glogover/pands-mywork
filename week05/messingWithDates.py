# Messing with dates
# Author: Marcin Kaminski

import datetime

my_date= datetime.datetime.now()
print(my_date)

day_of_the_week_integer = my_date.weekday()

""" 
weekday() function returns the integer mapping corresponding to the specified day
of the week.
Below listing shows the integer values corresponding to the day of the week.

0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
5 Saturday
6 Sunday

"""

print(day_of_the_week_integer)

if day_of_the_week_integer == 5 or day_of_the_week_integer == 6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")



