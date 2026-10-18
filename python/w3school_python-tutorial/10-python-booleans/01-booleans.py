# python booleans
"""
* booleans represent one of two values: True or False
"""

# boolean values

print(10 > 9)
print(10 == 9)
print(10 < 9)

"""
* when you run a condition in an if statement, python return True or False

sample
- print a message based on whether the condition is true or False
"""
a = 200
b = 33

if b < a:
    print("b is greater than a")
else:
    print("b is not greater than a")



# evaluate values and variables
"""
* the bool() function allows you to evaluate any value, and give you true or false in return

sample
- evaluate a string and a number
"""
print(bool("Hello"))
print(bool(15))


"""
sample
- evaluate two variables
"""
c = "Hello"
d = 15

print(bool(c))
print(bool(d))



# most values are true
"""
* almost any value is evaluated to 'true' if it has some sort of content
* any string is 'true', except empty strings
* any number is 'true', except 0
* any list, tuple, set, and dictionary are 'true', except empty ones

sample
- the following will return 'true'
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



# some values are false
"""
* in fact, there are not many values that evaluate to 'false', except empty values, such as (), [], {}, "", 
the number 0 and the value None.
* and of course the value 'false' evaluates to 'false'

sample
- the following will return 'false'
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
* one more value, or object in this case, evaluates to 'false', and that is if you have an object that is made from a class with a __len__ function that returns 0 or 'false'

sample:
"""
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))



# functions can return a boolean
"""
* you can create functions that returns a boolean value

sample
- print the answer of a function
"""
def myFunction():
    return True

print(myFunction())

"""
* you can execute code based on the Boolean answer of a function

sample
- print "YES" if the function returns True, otherwise print "NO"
"""
def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO")

"""
* python also has many built-in functions that return a boolean value, like the 'isinstance()' function, which can be used to determine if an object is of a certain data type

sample
- check if an object is a integer or not
"""
x = 200
print(isinstance(x, int))
print(isinstance(x, str))




































