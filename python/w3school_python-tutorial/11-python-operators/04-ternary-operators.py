# ternary operator
"""
* the ternary operator allows you to assign on value if a condition is true, and another if it is false

example
- assign the value "WEEKEND" if the number is higher than 5, otherwise "WORKDAY"
"""
num = 6
x = "WEEKEND" if num > 5 else "WORKDAY"
print(x)

"""
NOTE: the ternay operator is not an actual operator, it is a conditional expression, or a shorthand if statement
"""




# instead of Elif
"""
* the ternay operator can be used instead of "elif" in longer if statement

example
- Assign:
    - "Fri" if num is 5
    - "Sat" if num is 6
    - "Sun" if num  is 7
    - otherwise assign "WEEKEND"
"""

num2 = 6
x = "Fri" if num2 == 5 else "Sat" if num2 == 6 else "Sun" if num2 == 7 else "WEEKEND"

print(x)





