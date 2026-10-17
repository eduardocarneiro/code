# global variables
"""
* global variables can be used by everyone, both inside of functions and outside
"""

x = "awesome"

def myfunc():
    print("python is " + x)

myfunc()


"""
* if you create a variable with a same name inside a function, this variable will be local, and can only be used inside the function. 
* global variable with the same name will remain as it was, global and with the original value
"""

a = "awesome"

def myfunc2():
    a = "fantastic"
    print("python is " + a)

myfunc2()

print("python is " + a)



# the global keyword

"""
* normally , when you create a variable inside a function, that variable is local, and can only be used inside that function

* to create a global variable inside a function, you can use the "global" keyword
"""

def myfunc3():
    global b 
    b = "fantastic"

myfunc3()

print("python is " + b)


"""
* also use the "global" keyword if you want to change a global variable inside a function
* to change the value of a global variable inside a funciton, refer to the variable by using the "global" keyword

"""

c = "amazing"

def myfunc4():
    global c 
    c = "fantastic"
    print(c)

myfunc4()

print("python is " + c)


