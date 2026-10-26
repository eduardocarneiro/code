# python - shorthand if


# short hand if
"""
* if you have only one statement to execute, you can put it on the same line as the "if" statement 

example 
- on-line if statement 
"""
a = 5 
b = 2
if a > b: print("a is greater than b")



# short hand if ... else
"""
* if you have one statement for "if" and one for "else", you can put them on the same line using a conditional expression

example
- one-line if/else that prints a value

NOTE: this is called a "conditional expression" (sometimes known as a "ternary operator")
"""
a = 2
b = 330
print("A") if a > b else print("B")



# assign a value with if .. else 
"""
* you can also use a one-line "if/else" to choose a value and assign it to a variable 

* the syntax follows this pattern
    variable = value_if_true if conditional else value_if_false

example 
"""
a = 10
b = 20

bigger = a if a > b else b 
print("bigger is: ", bigger)



# multiple conditions on one line 
"""
* you can chain conditional expressions, but keep it short so it stays readable 

example 
- one line, three outcomes
"""
a = 330
b = 330 
print("A") if a > b else print("=") if a == b else print("B")



# practical examples
"""
* tenary operators are particularly useful for simple assignments and return statements

example 
- finding the maximum of two numbers 
"""
x = 15
y = 20
max_value = x if x > y else y 
print("Maximum value: ", max_value)


"""
example 
- setting a default value 
"""
username = ""
display_name = username if username else "Guest"
print("welcome", display_name)



# when to use shorthand if 
"""
* shorthand if statements and ternary operators should be used when
    - the condition and actions are simple
    - it improves code readability
    - you want to make a quick assignment based on a condition 


IMPORTANT: while shorthand if statement can make code more concise, avoid overusing them for complex conditions. Fo readability, use regular if-else statements when dealing with multiple lines of code or complex logic
"""













































