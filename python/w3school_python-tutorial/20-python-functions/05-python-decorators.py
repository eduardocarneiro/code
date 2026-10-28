# python - decorators 

"""
* decorators let you add extra behavior to a function, without changing the function's code

* a decorator is a function that takes another function as input and returns a new function 
"""



# basic decorator 
"""
* define the decorator first, then apply it with "@decorator_name" above the function

example:
- a basic decorator that uppercases the return value of the decorated function
"""
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())


"""
* by placing "@changecase" directly above the function definition, the function "myfunction" is being "decorated" with the "changecase"
function

* 
"""



# multiple decorator calls 
"""
* a decorator can be called multiple times. just place the decorator above the function you want to decorate 

example:
- using the "@changecase" decorator on two functions 
"""
print("\n")

def changecase2(func):
    def myinner():
        return func().upper()
    return myinner 

@changecase2
def myfunction2():
    return "Hello Sarah"

@changecase2
def otherfunction():
    return "I am speed"

print(myfunction2())
print(otherfunction())



# arguments in the decorated function
"""
* functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function

example:
- functions with arguments can also be decorated 
"""

def changecase3(abc):
    def fnc1(x):
        return abc(x).upper()
    return fnc1 


@changecase3
def my_func1(nam):
    return "Hello " + nam 

print(my_func1("John"))



# *args and **kwargs
"""
* sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add "*args, **kwargs" to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function 

example:
- secure the function with *args and **kwargs arguments 
"""
def changecase4(func):
    def fnc2(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return fnc2

@changecase4
def myfunction3(nam):
    return "Hello " + nam 

print (myfunction3("John"))



# decorate with arguments
"""
* decorators can accept their own arguments by adding another wrapper level

example:
- a decorator factory that takes an argument and transforms the casing based on the argument value 
"""
def changecase5(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase5(1)
def fnc3():
    return "Hello Linus"

print(fnc3())



# multiple decorators 
"""
* you can use multiple decorators on one function

* this is done by placing the decorator calls on top of each other 

* decortors are called in the reverse order, starting with the one closet to the function 

example:
- one decoraor for upper case, and one for adding a greeting 
"""
def changecase6(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase6
@addgreeting 
def fnc4():
    return "eoc"

print(fnc4())



# preserving function metadata
"""
* functions in python has metadata that can be accessed using the "__name__" and "__doc__" attributes

example:
- normally, a function's name can be returned with the "__name__" attribute 
"""
def myfunc1():
    return "have a great day!"

print(myfunc1.__name__)


"""
* but, when a function is decorated, the metadata of the original function is lost 

example:
- try returning the name from a decorated function and you will not get the same result
"""
def changecase7(func):
    def myinner():
        return func().upper()
    return myinner

@changecase7
def myfunc2():
    return "have a great day!"

print(myfunc2.__name__)



"""
* to fix this, python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring 

example:
- import "functools.wraps" to preserve the original function name and docstring 
"""
import functools

def changecase8(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner

@changecase8
def myfunc3():
    return "have a great day"

print(myfunc3.__name__)






























