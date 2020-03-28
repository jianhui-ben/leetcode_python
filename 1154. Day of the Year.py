
#Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

#Example 1:

#Input: date = "2019-01-09"
#Output: 9
#Explanation: Given date is the 9th day of the year in 2019.
#Example 2:

#Input: date = "2019-02-10"
#Output: 41

class Solution(object):

    import re
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year=date[:4]
        month= date[5:7]
        day= date[8:]
        days_per_month_365=[31,28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_per_month_366=[31,29,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]        
        if int(year)%4!=0:
            return sum(days_per_month_365[:int(month)-1])+int(day)
        elif int(year)%100!=0 or int(year)%400==0:
            return sum(days_per_month_366[:int(month)-1])+int(day)
        else:
            return sum(days_per_month_365[:int(month)-1])+int(day)
