# python - user input



# user input 
"""
* python allows for user input 

* that means we are able to ask the user for input 

* the following example asks for your name, and when you enter a name, it gets printed on the screen

example:
- ask for user input 
"""
print("\n")
print("Enter your name: ")
name = input()
print(f"Hello, { name }")

"""
NOTE: python stops executing when it comes to the "input()" function, and continues when the user has given some input 
"""



# using prompt 
"""
* in the example above, the user had to input their name on a new line. the python "input()" function has a "prompt" parameter, which acts as a message you can put in front of the user input, on the same line

example:
- add a message in front of the user input 
"""
name = input("Enter your name: ")
print(f"Hello, { name }")
print(f"Hello, { input("Enter your name: ")} ")



# multiple inputs 
"""
* you can add as many inputs as you want, python will stop execurting at each of them , waiting for user input 

example:
- multiple inputs
"""
name = input("Enter your name: ")
print(f"Hello, {name}")
fav1 = input("What is your favorite animal: ")
fav2 = input("What is your favorite color: ")
fav3 = input("What is your favorite number: ")
print(f" Do you want a {fav2} {fav1} with {fav3} legs?")



# input number 
"""
* the input from the user is treated as a string. even if, in the example above, you can input a number, the python interpreter will still treat it as a string 

* you can convert the input into a number with a "float()" function 

example:
- to find the square root, the input has to be converted into a number 
"""
import math 
x = input("Enter a number: ")

# find the square root of the number 
y = math.sqrt(float(x))
print(f"the square root of {x} is {y}")



# validate input 
"""
* it is a good practice to validate any input from the user. in the example above, an error will occur if the user inputs something other than a number 

* to avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "wrong input, please try again", and allowed to make a new input 

example:
- keep asking until you get a number 
"""
y = True 
while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x);
        y = False 
    except:
        print("wrong input, please try again.")

print("thank you")

















































