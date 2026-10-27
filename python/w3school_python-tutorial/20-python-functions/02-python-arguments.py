# python - function arguments 


# arguments 
"""
* information can be passed into function as arguments

* arguments are specified after the function name, inside the parentheses. you can add as many arguments as you want, just separate them with a comma

* the following example has a function with one argument (fname). when the function is called, we pass along a first name, which is used inside the function to print the full nam 

example: 
- a function with one argument 
"""

import re


def my_func(fname):
    print(fname + " Carneiro")

my_func("Eduardo")
my_func("Sarah")
my_func("Natty")



# parameters vs arguments 
"""
* the terms parameter and argument can be used for the same thing: information that are passed into a function

From a function perspective:
    - a "parameter" is a variable listed inside the parentheses in the function definition
    - an "argument" is the actual value that is sent to the function when it is called 

example:
"""
def my_func2(name): # name is a parameter
    print("Hello", name)

my_func2("eoc") # "eoc" is an argument



# number of arguments
"""
* by default, a function must be called with the correct number of arguments 

* if your function expects 2 arguments, you must call it with exactly 2 arguments


NOTE: if you try to call the function with the wrong number of arguments, you will get an error 

example:
- this function expects 2 arguments, and get 2 arguments 
"""
def my_func3(fname, lname):
    print("Hello " + fname + " " + lname)

my_func3("EOC", "Oliveira")
#my_func3("abc") # it will returns a error message



# default paramenter values 
"""
* you can assign default values to paramenters. if the function is called without an argument, it uses the default value 

example:
"""
def my_func4(name = "eoc"):
    print("Hello", name)

my_func4()
my_func4("Eduardo")



# keyword arguments
"""
* you can send arguments with the key = value syntax 

example:
"""
def my_func5(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_func5(animal = "dog", name = "natal")


"""
* this way, with keyword arguments, the order of the arguments does not matter 


NOTE: the phrase "keyword arguments" is often shortened to "kwargs" in python documentation 

example 
"""
def my_func6(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_func6(name = "sabrina", animal = "dog")



# positional arguments
"""
* when you call a function with arguments without using kerywords, they are called positional arguments

* positional arguments must be in the correct order 

example:
"""
def my_func7(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)


my_func7("dog", "buddy")


"""
* the order matters with position arguments 

example:
- switching the order changes the result
"""
def my_func8(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_func7("buddy", "cat")



# mixing positional and keyword arguments
"""
* you can mix positional and keyword arguments in a function call

* however, positional arguments must come before keyword arguments 

example:
"""
def my_func8(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_func8("dog", name = "Buddy", age = 5)



# passing different data types
"""
* you can send any data type as an argument to a function (string, number, list, dictionary, etc)

* the data type will be preserved inside the function

example:
- sending a list as an argument 
"""
def my_func9(fruits):
    for fruit in fruits:
        print(fruit) 

my_fruits = ["apple", "banana", "cherry"]

my_func9(my_fruits)


"""
example:
- sending a dictionary as an argument 
"""
def my_func10(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "eoc", "age": 41}
my_func10(my_person)



# return values 
"""
* functions can return values using return statement 

example 
"""
def my_func11(x, y):
    return x + y 

result = my_func11(5, 3)
print(result)



# returning different data types 
"""
* functions can return any data type, including lists, tuples, dictionaries, and more 

example 
- a function that returns a list 
"""
def my_func12():
    return ["apple", "banana", "cherry"]

fruits = my_func12()
print(fruits[0])
print(fruits[1])
print(fruits[2])


"""
example:
- a function that returns a tuple 
"""
def my_func13():
    return (10, 20)

x, y = my_func13()
print("x: ", x)
print("y: ", y)



# positional-only arguments
"""
* you can specify that a function can have ONLY positional arguments

* to specify positional-only arguments, add ", /" after the arguments

NOTE: without the ", /" you are actually allowed to use keyword arguments even if the function expects positional arguments 

example
"""
def my_func14(name, /):
    print("Hello", name)

my_func14("eoc")


"""
* with ",/" , you will get an error if you try to use keyword arguments

example 
"""
def my_func15(name, /):
    print("Hello , ", name)

#my_func15(name = "eoc") # it will get an error message



# keyword-only arguments
"""
* to specify that a function can have only keyword arguments, add "*," before the arguments

NOTE: without "*," , you are allowed to use positional arguments even if the function expects keyword arguments

example 
"""
def my_func16(*, name):
    print("Hello: ", name)

my_func16(name = "eoc")


"""
* with "*," , you will get an error if you try to use positional arguments 

example 
"""
def my_func17(*, name):
    print("hello, ", name)

#my_func17("eoc") # will get a error message 



# combining positional-only and keyword-only 
"""
* you can combine both argumens types in the same function 

* arguments before / are positional-only, and arguments after * are keyword-only 

example: 
"""
def my_func19(a, b, /, *, c, d):
    return a + b + c + d

result = my_func19(5, 10, c = 15, d = 30)
print(result)






































