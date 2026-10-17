# string format
"""
* in python we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

* We can combine strings and numbers by using f-strings or the format() method
"""



# f-strings
"""
* f-strings was introduced in python 3.6 and is now the preferred way of formatting strings
* to specify a string as an f-string, simply put an "f" in front of th string literal, and add curly brackets {} as placeholders for variables and other operations
"""

age = 41
txt = f"My name is Eduardo, I am {age}"
print(txt)
print(f"My name is Eduardo, I am {age}")



# placeholders and modifiers
"""
* placeholders can contain variables, operations, functions, and modifiers to format the value

sample
- add a placeholder for the price variable 
"""
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
* placeholder can include a modifier to format the value
* modifier is included by adding a colon ":" followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

sample
- display the price with 2 decimals
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

"""
* placeholder can contain python code, like math operations

sample
- perform a math operation in the placeholder and return the result
"""
txt = f"The price is {20 * 50} dollars"
print(txt)
