# python - *args and **kwargs 


# *args and **kwargs 
"""
* by default, a function must be called with the correct number of arguments 

* however, sometimes you may not know how many arguments that will be passed into your function 

* *args and **kwargs allow functions to accept a unknown number of arguments 
"""



# arbitrary arguments - *args 
"""
* if you do not know how many arguments will be passed into your function, add a * before the parameter name

* this way, the function will receive a tuple of arguments and can access the items accordingly 


NOTE: Arbitrary Arguments are often shortened to *args in python documentation 

example:
- using *args to accept any number of arguments 
"""


def func1(*kids):
    print("the youngest child is " + kids[2])

func1("EOC", "NAGC", "SGC")



# what is *args 
"""
* the *args paramenter allows a function to accept any number of positional arguments

* inside the function, args becomes a tuple containing all the passed arguments 

example 
- accessing individual arguments from *args 
"""
def func2(*args):
    print("Type: ", type(args))
    print("First argument:", args[0])
    print("Second argument: ", args[1])
    print("all arguments:", args)

func2("eoc", "nagc", "sgc")



# using *args with regular arguments 
"""
* you can combine regular parameters with *args 

* regular parameters must come before *args 

NOTE: in this example, "Hello" is assigned to "grettings", and the rest are collected in "names" 
example: 
"""
def func3(greetings, *names):
    for name in names:
        print(greetings, name)

func3("hello", "eoc", "nagc", "sgc")



# practical example with *args 
"""
* *args is useful when you want to create flexible functions

example:
- a function that calculates the sum of any number of values 
"""
def func4(*numbers):
    total = 0 
    for num in numbers:
        total += num 

    return total 

print(func4(1, 2, 3))
print(func4(10, 20, 30, 40))
print(func4(5))


"""
example:
- finding the maximum value 
"""
print("\n")

def func5(*numbers):
    if len(numbers) == 0:
        return None 
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(func5(3, 7, 2, 9, 1))



# arbitrary keyword arguments - **kwargs 
"""
* if you do not know how many keyword arguments will be passed into your function, add two asterisks "**" before the parameter name 

* this way, the function will receive a dictionary of arguments and can access the items accordingly 

NOTE: arbitrary keyword arguments are often shortened to **kwargs in python documentation

example:
- using **kwargs to accept any number of keyword arguments 
"""
def func6(**kid):
    print("His last name is " + kid["lname"])

func6(fname = "Tobias", lname = "Snow")



# what is **kwargs 
"""
* the "**kwargs" parameter allows a function to accept any number of keyword arguments 

* inside the function, "kwargs" becomes a dictionary containing all the keyword arguments 

example:
- accessing values from **kwargs 
"""
def func7(**myvar):
    print("type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

func7(name = "Tobias", age = 30, city = "Bergen")



# using **kwargs with regular arguments 
"""
* you can combine regular parameters with **kwargs

* regular parameters must come before **kwargs 

example:
"""
def func8(username, **details):
    print("Username:", username)
    print("additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

func8("eoc", age = 41, city = "São Paulo", hobby = "coding")



# combining *args and **kwargs

"""
* you can use both *args and **kwargs in the same function 

the order must be:
    1. regular parameter
    2. *args
    3. **kwargs 

example:
"""
def func9(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func9("User Info", "eoc", "sgc", age = 7, city = "Dublin")



# unpacking arguments
"""
* the "*" and "**" operators can also be used when "calling" functions to unpack (expand) a list or dictionary into separate arguments 

"""



# unpacking list with *
"""
* if you have values stored in a list, you can use * to unpack them into individual arguments 

example:
- using * to unpack a list into arguments 
"""
def func10(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = func10(*numbers) # same as: func10(1, 2, 3)
print(result)



# unpacking dictionaries with **
"""
* if you have keyword arguments stored in a dictionary, you can use ** to unpack them 

example:
- using ** to unpack a dictionary into keyword arguments 
"""
def func11(fname, lname):
    print("hello", fname, lname)

person = {"fname": "eoc", "lname": "carneiro"}
func11(**person) # same as: func11(fname="eoc", lname="carneiro")


"""
NOTE: Use * and ** in function definitions to "collect" arguments, and use them in function calls to unpack arguments 
"""
































































