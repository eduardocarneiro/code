# python if statement

# python conditions and if statements
"""
* python supports the usual logical conditions from mathematics

    - equals:                   a == b
    - not equals:               a != b
    - less than:                a < b
    - less than or equal to:    a <= b
    - greater than:             a > b
    - greater than or equal to: a >= b

* these conditions can be used in several ways, most commonly in "if statement" and loops

* an "if statement" is written by using the "if" keyword 

example
- if statement 
"""
a = 33
b = 200

if b > a:
    print("b is greater than a")



# how if statement work
"""
* the if statement evaluates a condition (an expression that results in True or False). If the condition is True, the code block inside the if statement is executed. If the condition is false, the code block is skipped 

example
- checking if a number is positive
"""
number = 15
if number > 0:
    print("the number is positive")



# indentation
"""
* python relies on indentation (whitespace at the beginning of a line) to define scope in the code. other programming languages often use curly-brackets for this purpose

example
- if statement, without indentation (will raise an error)

NOTE: you can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block 
"""
a = 33 
b = 200
if b > a:
#print("b is greated than a") # will get an error
    print("b is greated than a") # will get an error



# multiple statements in if block 
"""
* you can have multiple statements inside an if block. all statements must be indented at the same level

example
- multiple statements in an if block 
"""
age = 20 
if age >= 18:
    print("you are an adult")
    print("you can vote")
    print("you have full legal rights")



# using variables in conditions 
"""
* boolean variables can be used directly in if statements without comparison operators 

example
- using a boolean variable 
"""
is_logged_in = True 
if is_logged_in:
    print("Welcome back!")


"""
* python can evaluate many types of values as True or False in an if statement

* zero (0), empty string (""), None, and empty collections are treated as False. Everything else is treated as True 

* this includes positive numbers(5), negative numbers(-3), and any non-empty string (even "False" is treated as True, because it's an non-empty string)
"""








































