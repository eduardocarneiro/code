# python - functions


# python functions
"""
* a function is a book of code which only runs when it is called 

* a function can return data as a result 

* a function helps avoiding code repetition 
"""



# creating a function 
"""
* in python, a function is defined using the "def" keyword, followed by a function name and parentheses

example:
def my_function():
    print("hello from a function")

* this creates a function named "my_function" that prints "hello from a function" when called

NOTE: the code inside the function must be indented. python uses indetation to define code blocks.
"""



# calling a function 
"""
* to call a function, write its name followed by parentheses 

example:
"""
def my_function():
    print("hello from a function")

my_function()


"""
* you can call the same function multiple times

example: 
"""
def my_function():
    print("\n")
    print("hello from a functions")

my_function()
my_function()
my_function()



# function names 
"""
* function names follow the same rules as variable names in python 
    - a function name must start with a letter or underscore
    - a function name can only contain letters, numbers, and underscores 
    - function names are case-sensitive (myFunction and myfunction are different)

example
- valid function names 

calculate_sum()
_private_function()
myFunction2()


NOTE: it is good practice to use descriptive names that explain what the functin does
"""



# why use functions
"""
* imagine you need to convert temperature from Fahrenheit to Celsius several times in your program. without functions you would have to write the same calculation code repeatedly

example 
- without functions - repetitive code 
"""
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


"""
* with functions, you write the code once and reuse its
example
- with functions - reusable code 
"""
print("\n")

def fahrenheit_to_celsius(num):
    return (num - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))



# return values
"""
* functions can send data back to the code that called them using the "return" statement 

* when a function reaches a "return" statement, it stops executing and sends the result back

NOTE: if a function does not have a "return" statement, it returns "None" by default 

example
- a function that returns a value
"""
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)


"""
* you can use the returned value directly

example
- using the return value directly 
"""
def get_greeting2():
    return "Hello from a function again"

print(get_greeting2())



# the pass statement 
"""
* function definitions cannot be empty. if you need to create a function placeholder without any code, use the "pass" statement 

* the "pass" statement if often used when developing, allowing you to define the structure first and implement details later

example
"""
def my_function2():
    pass

my_function2()













































































