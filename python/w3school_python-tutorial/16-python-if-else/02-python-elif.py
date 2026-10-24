# python - elif statement


# the elif keyword
"""
* the "elif" keyword is python's way of saying "if the previous conditions were not true, then try this condition"

* the "elif" keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True 


NOTE: in this example "a" is equal to "b", so the first condition is not true, but the "elif" condition is true, so we print to screen that "a and b are equal"

example
"""
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")



# multiple elif statements
"""
* you can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true 

example
- testing multiple conditions 


NOTE: in this example, the program checks each condition in order. Since score is 75, it prints "Grade: C" (the first condition that evaluates to true)
"""

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")



# how elif works
"""
* when you use "elif", python evaluates the conditions from top to bottom. as soon as it finds a condition that is true, it executes that block and skips all remaining conditions

IMPORTANT: only the first True condition will be executed. even if multiple conditions are True, python stops after executing the first matching block

example
- categorizing age groups
"""
age = 25 

if age > 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are an adult")
elif age >= 65:
    print("you are a senior")



# when to use elif 
"""
* use "elif" when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate "if" statements because python stops checking once it finds a True condition 

example
- day of the week checker
"""

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")



































