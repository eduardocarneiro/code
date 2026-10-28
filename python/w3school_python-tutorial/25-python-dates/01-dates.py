# python - datetime



# python dates 
"""
* a date in python is not a data tupe of its own, but we can import a module named "datetime" to work with dates as date objects

example:
- import the datetime module and display the current date 
"""
import datetime 

x = datetime.datetime.now()
print(x)



# date output
"""
* when we execute the code from the example above the result will be

 ----------------------------
| 2026-10-28 16:05:08.034377 |
 ----------------------------

 * the date contains year, month, day, hour, minute, second, and microsecond 

 * the "datetime" module has many methods to return information about the date object 

 * here are a few examples, you will learn more about them later in this chapter 

 example:
- return the uear and name of weekday
"""
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))



# creating data objects
"""
* to create a date, we can use the "datetime()" class (constructor) of the "datetime" module 

* the "datetime()" class requires three parameters to create a date: year, month, day 

example:
- create a date object 
"""
print("\n")
import datetime 

x = datetime.datetime(2020, 5, 17)
print(x)


"""
* the "datetime()" class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone) 
"""



# the strftime() method 
"""
* the "datetime" object has a method for formatting date objects into readable strings 

* the method is called "strftime()", and takes one parameter, "format", to specify the format of the returned string 

example:
- display the name of the month 
"""
import datetime

x = datetime.datetime(1985, 9, 10)

print(x.strftime("%B"))



"""
* a reference of all the legal format codes


 -----------------------------------------------------------------------------------------------------------
| directive     description                                                     example                     |
| %a            weekday, short version                                          wed                         |
| %A            weekday, full version                                           Wednesday                   |
| %w            weekday as a number 0-6, 0 is sunday                            3                           |
| %d            day of month 01-31                                              31                          |
| %b            month name, short version                                       Dec                         |
| %B            month name, full version                                        December                    |
| %m            month as a number 01-12                                         12                          |
| %y            year, short version, without century                            18                          |
| %Y            year, full version                                              2026                        |
| %H            hour 00-23                                                      16                          |
| %I            hour 00-12                                                      05                          |
| %p            AM/PM                                                           PM                          |
| %M            minute 00-59                                                    35                          |
| %S            second 00-59                                                    08                          |
| %f            microsendo 000000-999999                                        543211                      |
| %z            UTC offset                                                      +0100                       |
| %Z            timezone                                                        UTC-3                       |
| %j            day number of year 001-366                                      365                         |
| %U            week number of year, sunday as the first day of week, 00-53     52                          |
| %W            week number of year, monday as the first day of week, 00-53     52                          |
| %c            local version of date and time                                  Mon Dec 31 17:41:00 2018    |
| %C            century                                                         20                          |
| %x            local version of date                                           12/31/18                    |
| %X            local version of time                                           17:41:00                    |
| %%            A % character                                                   %                           |
| %G            ISO 8601 year                                                   2026                        |
| %u            ISO 8601 weekday (1-7)                                          1                           |
| %V            ISO 8601 weeknumber (01-53)                                     01                          |
 -----------------------------------------------------------------------------------------------------------


"""



















































