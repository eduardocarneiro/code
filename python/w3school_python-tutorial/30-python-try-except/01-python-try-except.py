# python - try - except 
"""
* the "try" block lets you test a block of code for errors 

* the "except" block lets you handle the errors

* the "else" block lets you execute code when there is no errors

* the "finally" block lets you execute code, regardless of the result of the try- and except blocks
"""



# exception handling 
"""
* when an error occurs, or exception as we call it, python will normally stop and generate an error message

* these exceptions can be handled using the "try" statement 

example:
- the "try" block will generate an exception, because "x" is not defined 
"""
try:
    print(x)
except:
    print("An exception occurred")
       

"""
* since the try block raises an error, the except block will be executed 

* without the try block, the program will crash and raise an error 

example:
- this statement will raise an error, because "x" is not defined 
"""
#print(x)



# many exceptions
"""
* you can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error

example:
- print one message if the try block raises a "NameError" and another for other errors 
"""
try: 
    print(x)
except NameError:
    print("variable 'x' is not defined")
except:
    print("something else went wrong")

"""

NOTE: see more Error types in our "Python built-in Exceptions Reference" - w3schools.com/python/python_ref_exceptions.asp
"""



# else 
"""
* you can use the "else" keyword to define a block of code to be executed if no errors were raised 

example:
- in this example, the "try" block does not generate any error
"""
try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")



# finally 
"""
* the "finally" block, if specified,w ill be executed regardless if the try block raises an error or not 

example:
- try to open and write to a file that is not writable 
"""
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")


"""
* the program can continue, without leaving the file object open 
"""



# raise an exception 
"""
* as a python developer you can choose to throw an exception if a contition occurs

* to throw (or raise) an exception, use the "raise" keyword

example:
- raise an error and stop the program if x is lower than 0
"""
#x = -1 
#
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")


"""
example:
- raise a TypeError if x is not an integer 
"""
print("\n")
y = "hello"
print(y)
if not type(y) is int:
    raise TypeError("only integers are allowed")



