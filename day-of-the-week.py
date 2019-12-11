'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
'''
import calendar
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        if (calendar.weekday(year, month, day)) == 0:
            return "Monday"
        elif (calendar.weekday(year, month, day)) == 1:
            return "Tuesday"
        elif (calendar.weekday(year, month, day)) == 2:
            return "Wednesday"
        elif (calendar.weekday(year, month, day)) == 3:
            return "Thursday" 
        elif (calendar.weekday(year, month, day)) == 4:
            return "Friday"
        elif (calendar.weekday(year, month, day)) == 5:
            return "Saturday"
        elif  (calendar.weekday(year, month, day)) == 6:
            return "Sunday"
Test = Solution()
print Test.dayOfTheWeek(19,7,1999)

