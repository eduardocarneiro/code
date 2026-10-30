# python - none
"""
* "None" is a special constant in python that represents the absence of a value 

* its data type is "NoneType", and "None" is the only instance of a "NoneType" object
"""



# nonetype 
"""
* variables can be assigned "None" to indicate "no value" or "not set"

example:
- assign and display a "None" value 
"""
from contextlib import redirect_stdout
import types
from typing import overload


x = None 
print(x)



"""
* Use "type()" to see the type of a "None" value 

example:
- assign and print the data type of a "None" value 
"""
x = None 
print(type(x))
overload



# comparing to none 
"""
* to compare a value to "None", use the identify operator "is" or "is not"

example:
- use the identity operator "is" for comparisons with "None"
"""
result = None 
if result is None:
    print("No result yet")
else:
    print("Result is ready")


"""
example:
- similar example, but using "is not" instead 
"""
result = None 
if result is not None:
    print("Result is ready")
else:
    print("No result yet")



# true or false 
"""
* "None" evaluates to "False" in a boolean context 

example:
- check truthiness
"""
print(bool(None))



# functions returning none 
"""
* functions that do not explicitly return a value return "None" by default 

example:
- a function without a return statement returns "None"
"""
def func():
    x = 5

x = func()
print(x)




















































