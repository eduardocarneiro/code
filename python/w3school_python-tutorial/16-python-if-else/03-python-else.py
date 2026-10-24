# python else statement


# the else keyword
"""
* the "else" keyword catches anything which is not caught by the preceding conditions

* the "else" statement is executed when the "if" condition (and any elif conditions) evaluate to False


NOTE: in this example "a" is greater than "b", so the first condition is not True, also the the "elif" condition is not True, so we go to the "else" condition and print to screen that "a is greater than b"

example
"""
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



# else without elif
"""
* you can also have an "else" without the "elif"


NOTE: this creates a simple two-way choice: if the condition is true, execute on block; otherwise, execute the else block

example 
"""
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")



# how else works
"""
* the "else" statement provides a default action when none of the previous conditions are True. think of it as a 'catch-all' for any scenario not covered by your "if" and "elif" statements


NOTE: the "else" statement must come last. you cannnot have an elif after an "else"

example 
- checking even or odd numbers
"""
number = 7 

if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")



# complete if-elif-else chain 
"""
* you can combine "if", "elif", and "else" to create a comprehensive decision-making structure

example
- temperature classifier 
"""

temperature = 5

if temperature > 30:
    print("it is hot outside")
elif temperature > 20: 
    print("it is warm outside")
elif temperature > 10:
    print("it is cold outside")
else:
    print("it is REALLY cold outside")



# else as fallback
"""
* the "else" statement acts as a fallback that executes when none of the preceding conditions are true. this makes it useful for error handling, validation and providing default values

example
- validating user input
"""
username = "eoc"

if len(username) > 0:
    print(f"welcome, {username}")
else:
    print(f"Error: username cannot be empty")









































