# python - string formatting 

"""
* f-string was introduced in python 3.6, and is now the preferred way of formatting strings

* before python 3.6 we had to use the "format()" method 
"""



# f-strings 
"""
* f-string allows you to format selected parts of a string 

* to specify a string as an f-string, simply put "f" in front of the string literal, like this 

example:
- create an f-string 
"""
txt = f"The price is 49 dollars"
print(txt)



# placeholders and modifiers 
"""
* to format values in an f-string, add placeholders "{}", a placeholder can contain variables, operations, functions, and modifiers to format the value 

example:
- add a placeholder for the "price" variable 
"""
price = 59 
txt = f"The price is {price} dollars"
print(txt)



"""
* a placeholder can also include a modifier to format the value 

* a modifier is included by adding a colo ":" followed by a legal formatting type, like ".2f" which means fixed point number with 2 decimals 

example:
- display the price with 2 decimals 
"""
print("\n")
price = 109
txt = f"The price is {price:.2f} dollars"
print(txt)


"""
* you can also format a value directly without keeping it in a variable 

example:
- display the value "95" with 2 decimals 
"""
print("\n")
txt = f"The price is {95:.2f} dollars"
print(txt)



# perform operations in f-strings 
"""
* you can perform python operations inside the placeholders 

* you can do math operations 

example:
- perform a math operation in the placeholder, and return the result 
"""
print("\n")

a = 10
b = 3 
txt = f"The price is ${ a * b:.2f} dollars"
print(txt)


"""
* you can perform "if..else" statements inside the placeholders 

example:
- return "expensive" if the price is over 50, otherwise return "cheap"
"""
price1 = 49
price2 = 51
target = 50
txt1 = f"It is very {'Expensie' if price1 > target else 'Cheap'}"
txt2 = f"It is very {'Expensie' if price2 > target else 'Cheap'}"

print(txt1)
print(txt2)



# execute functions in f-strings 
"""
* you can execute functions inside the placeholder 

example:
- use the string method "upper()" to convert a value into upper case letters
"""
print("\n")
fruit = "apples"
print(fruit)
txt = f"I love {fruit.upper()}"
print(txt)


"""
* the function does not have to be a built-in python method, you can create your own functions and use them 

- create a function that converts feet into meters 
"""

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)



# more modifiers 
"""
* at the beginning of this chapter we explained how to use the ".2f" modifier to format a number into a fixed point number with 2 decimals

* there are several other modifiers that can be used to format values 

example:
- use a comma as a thousand separator
"""
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)



"""
* here is a list of all formatting types


 -------------------------------------------------------------------------------------------------------------------
| formatting types                                                                                                  |
| :<        left aligns the result (within the available space)                                                     |
| :>        right aligns the result (within the available space)                                                    |
| :^        center aligns the result (within the available space)                                                   |
| :=        places the sign to the left most position                                                               |
| :+        use a plus sign to indicate if the result is positive or negative                                       |
| :-        use a minus sign for negative values only                                                               |
| :         use a space to insert an extra space before positive numbers (and a minus sign before negative numbers) |
| :,        use a comman as a thousand separator                                                                    |
| :_        use a underscore as a thousand separator                                                                |
| :b        binary format                                                                                           |
| :c        converts the value into the corresponding unicode character                                             |
| :d        decimal format                                                                                          |
| :e        scientific format, with a lower case e                                                                  |
| :E        scientific format, with an upper case E                                                                 |
| :f        fix point number format                                                                                 |
| :F        fix point number format, in uppercase format (show "inf", and "nan", as "INF", and "NAN")               |
| :g        general format                                                                                          |
| :G        general format (using a upper case E for scientific notations)                                          |
| :o        octal format                                                                                            |
| :x        hex format, lower case                                                                                  |
| :X        hex format, upper case                                                                                  |
| :n        number format                                                                                           |
| :%        percentage format                                                                                       |
 -------------------------------------------------------------------------------------------------------------------
"""



# string format() 
"""
* before python 3.6 we used the "format()" method to format strings 

* the "format()" method can still be used, but f-string are faster and the preferred way to format strings 

* the next examples in this page demonstrates how to format strings with the "format()" method 

* the "format()" method also uses curly brackets as placeholders {}, but the syntax is slightly different 

example:
- add a placeholder where you want to display the price 
"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


"""
* you can add parameters inside the curly brackets to specify how to convert the value 

example:
- format the price to be displayed as a number with two decimals 
"""
print("\n")
price = 25
txt = "The price is {:.2f} dollars"
print(txt.format(price))


"""
* check out all formatting "string format() refenrece - https://www.w3schools.com/python/ref_string_format.asp"
"""




# multiple values 
"""
* if you want to use more values, just add more values to the format() method 

 -----------------------------------------
| print(txt.format(price, itemno, count)) |
 -----------------------------------------

* and add more placeholders 

example: 
"""
quantity = 3 
itemno = 567 
price = 49 
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))



# index numbers 
"""
* you can use index numbers (a number inside the curly brackets {0} to be sure the values are placed in the correct placeholders)

example:
"""
quantity = 3
itemno = 450
price = 25 
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


"""
* also, if you want to refer to the same value more than once, use the index number 

example:
"""
age = 41
name = "EOC"
txt = "His name is {1}. {1} is {0} years old"
print(txt.format(age, name))



# named indexes 
"""
* you can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use name when you pass the parameter values "txt.format(carname = "Ford)"

example:
"""
print("\n")

myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))









































