# python - scope 


# scope 
"""
* a variable is only available from inside the region it is created. this is called scope
"""



# local scope
"""
* a variable created inside a function belongs to the "local scope" of that function and can only be used inside that function 

example:
- a variable created inside a function is available inside that function 
"""
def fnc1():
    x = 300
    print(x)

fnc1()



# function inside function 
"""
* as explained in the example above, the variable "x" is not available outside the function, but it is available for any function inside the function

example:
- the local variable can be accessed from a function within the function 
"""
def fnc2():
    x = 300
    def fnc():
        print(x)
    fnc()

fnc2()



# global scope
"""
* a variable created in the main body of the python code is a global variable and belongs to the global scope 

* global variables are available from within any scope, global and local 

example:
- a variable created outside of a function is global and can be used by anyone 
"""
print("\n")
x = 300 

def fnc3():
    print(x)

fnc3()
print(x)



# naming variable
"""
* if you operate with the same variable name inside and outside of a function, python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function)

example:
- the function will print the local "x", and then the code will print the global "x"
"""
print("\n")

x = 300 

def fnc4():
    x = 200
    print(x)

fnc4()
print(x)



# global keyword
"""
* if you need to create a global variable, but are stuck in the local scope, you can use the global keyword 

* the "global" keyword makes the variable global

example:
- if you use the "global" keyword, the variable belongs to the global scope 
"""
def fnc5():
    global x
    x = 450

fnc5()
print(x)



"""
* also, use the "global" keyword if you want to make a change to a global variable inside a function

example:
- to change the value of a global variable inside a function, refer to the variable by using the "global" keyword 
"""
print("\n")
x = 500

def fnc6():
    global x
    x = 1985

fnc6()
print(x)



# nonlocal keyword 
"""
* the "nonlocal" keyword is used to work with variable inside nested functions

* the "nonlocal" keyword makes the variable belong to the outer function 

example:
- if you use "nonlocal" keyword, the variable will belong to the outer function 
"""
def fnc7():
    x = "jane"
    def nested_fnc1():
        nonlocal x
        x = "hello"
    nested_fnc1()
    return x 

print(fnc7())



# the LEGB rule 
"""
* python follows the LEGB rule when looking up variable names, and searches for them in this order:

    1. Local        - inside the current function
    2. Enclosing    - inside enclosing functions (from inner to outer)
    3. Global       - at the top level of the module
    4. Built-in     - in python's built-in namespace

example:
- understanding the LEGB rule 
"""
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

































