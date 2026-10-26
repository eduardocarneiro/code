# python - pass statement


# the pass statement 
"""
* "if" statements cannot be empty, but it you for some reason have an "if" statement with no content, put in the "pass" statement to avoid getting an error

NOTE: the "pass" statement is a null operation - nothing happens when it executes. it serves as a placeholder
example
"""

a = 33
b = 200

if b > a:
    pass



# why use pass 
"""
* the "pass" statement is useful in several situations
    - when you are creating code structur but have not implemented the logic yet 
    - when a statement is required syntactically but no action is needed
    - as a placeholder for future code during development
    - in empty functions or classes that you plan to implement later 
"""



# pass in development
"""
* during development, you might want to sketch out your program structure before implementing the details. the "pass" statement allows you to do this wihtout syntax errors 

example 
- placeholder for future implementation
"""
age = 200

if age < 18:
    pass # TODO: add underage logic later 
else:
    print("access granted")



# pass vs comments 
"""
* a comment is ignored by python, but "pass" is an actual statement that gets executed (though it does nothing). you need "pass" where python expects a statement,not just a comment 

example
- this will cause an error (empty code block)

# code
score = 85 
if score > 90:
    #this is excellent
# this will raise an indentationError
"""



# pass in other contexts 
"""
* while we focus on "pass" with if statements here, it is also commonly used with loops, functions and classes

example
- using pass with functions 
"""
def calculate_discount(price):
    pass # TODO: Implement discount logic 

calculate_discount(10)

