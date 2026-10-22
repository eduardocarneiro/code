# list comprehension
"""
* list comprehension offers a shorter syntax when yuo want to create a new list based on the values of an existing list

Example:
based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
without list comprehension you will have to write a "for" statement with a conditional test inside 

example
"""
from types import new_class


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

"""
* with list comprehension you can do all that with only one line of code 

example 
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)



# the syntax
"""
* newlist = [ expression for item in iterable if condition == True ]

* the return value is a new list, leaving the old list unchanged
"""



# condition
"""
* the condition is lie a filter that only accepts the items that evaluate to "True"

example 
- only accept items that are not "apple"

NOTE: the condition 'if x != "apple"' will return "True", for all elements other than "apple", making the new list contain all fruits except "apple"
"""
print("condition")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

"""
* the condition is optional and can be omitted

example
- with no if statement 
"""
print("condition without 'if'")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)



# iterable
"""
* the iterable can be any iterable object, like a list, tuple, set etc 

example 
- you can use the "range()" function to create an iterable 
"""
print("iterable")
newlist = [i for i in range(10)]
print(newlist)


"""
* same example, but with a condition 

example 
- accept only numbers lower than 5
"""
print("iterable with 'if' ")
newlist = [i for i in range(10) if i < 5]
print(newlist)



# expression
"""
* the expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list 

example 
- set the values in the new list to upper case
"""
print("expression")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)


"""
* the expression can also contain conditions, not like a filter, but as a way to manipulate the outcome

example 
- return "orange" instead of "banana"

NOTE: It will return the item if it is not banana, if it is banana return orange 
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)











