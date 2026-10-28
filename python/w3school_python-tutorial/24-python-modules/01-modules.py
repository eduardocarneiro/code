# python - modules 



# what is a module 
"""
* consider a module to be the same as a code library 

* a file containing a set of functions you want to include in your application 
"""



# create a module 
"""
* to create a module just save the code you want in a file with the file extension ".py"

example:
- save the code in a file named mymodule.py

 ---------------------------
| def greeting(name):       |
|   print("Hello, " + name) |
 ---------------------------
"""



# use a module 
"""
* now we can use the module we just created, by using the "import" statement 

example:
- import the module named mymodule, and call the greeting function 
"""
import mymodule

mymodule.greeting("EOC")


"""
NOTE: when using a function from a module, use the syntax: module_name.function_name 
"""



# variables in module 
"""
* the module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)

example:
- save this code in the file mymodule.py 

 ------------------------
| person1 = {            |
|    "name": "eoc",      |
|    "age": 41,          |
|    "contry": "Brazil"  |
| }                      |
 ------------------------

"""



"""
example:
- import the module named mymodule, and access the person1 dictionary 
"""
#import mymodule

a = mymodule.person1["age"]
print(a)



# naming a module 
"""
* you can name the module file whatever you like, but it must have the file extension ".py"
"""



# re-naming a module 
"""
* you can create an alias when you import a module, by using the "as" keyword 

example:
- create an alias for mymodule called mx
"""
import mymodule as mx 
a = mx.person1["country"]
print(a)



# built-in modules 
"""
* there are several built-in modules in python, which you can import whenever you like 

example
- import and use the "platform module"
"""
import platform 

x = platform.system()
print(x)



# using the dir() function 
"""
* there is a built-in function to list all the function names (or variable names) in a module. the "dir()" function 


NOTE: the "dir()" function can be used on all modules, also the ones you create yourself

example:
- list all the defined names belonging to the platform module 
"""
import platform

x = dir(platform)
print(x)

print("\n")
y = dir(mymodule)
print(y)



# import from module 
"""
* you can choose to import only parts from a module, by using the "from" keyword 

example:
- the module named mymodule2 has one funcion an one dictionary

 ---------------------------
| def greeting(name):       |
|  print("Hello, " + name)  |
|                           |
|  person1 = {              |
|    "name": "John",        |
|    "age": 36,             |
|    "country": "Norway"    |
|  }                        |
 ---------------------------
"""

"""
example:
- import only the person1 dictionary from the module 
"""
from mymodule2 import person1
print(person1["name"])


"""
NOTE: when importing using the "from " keyword, do not use the module name when referring to elements in the module. person1

example:
person1["age"], not mymodule2.person1["age"]
"""
















































