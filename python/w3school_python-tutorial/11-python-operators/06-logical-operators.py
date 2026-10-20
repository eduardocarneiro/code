# logical operators
"""
* logical operators are used to combine conditional statements


 -----------------------------------------------------------------------------------------------------
| operator      description                                                     example               |
| and           returns "true" if both statements are "true"                    x < 5 and x < 10      |
| or            returns "true" if one of the statements is "true"               x < 5 or x < 4        |
| not           reverse the result, returns "false" if the result is "true"     not(x < 5 and x < 10) |
 -----------------------------------------------------------------------------------------------------

"""

"""
example
- test if a number is greater than 0 "and" less than 10
"""
x = 5
print(x > 0 and x < 10)


"""
example
- test if number is less than 5 "or" greater than 10
"""
x = 5
print(x < 5 or x > 10)


"""
example
- reverse the result with "not"
"""
print(not(x > 3 and x < 10))


