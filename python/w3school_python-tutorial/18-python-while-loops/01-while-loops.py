# python - while loops


# python loops
"""
* python has two primitive loop commands:
    - while loops
    - for loops 
"""



# the while loop 
"""
* with the "while" loop we can execute a set of statements as long as a condition is true

example
- print "i" as long as "i" is less than 6

NOTE: remember to increment "i", or else the loop will continue forever
"""
i = 0

while i < 6:
    print(i)
    i +=1



"""
* the "while" loop requires relevant variables to be ready, in this example we need to define an indexing variable, "i", which we set to "1"
"""



# the break statement
"""
* with the "break" statement we can stop the loop even if the while condition is true 

example 
- exit the loop when "i" is 3
"""
print("\n")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



# the continue statement
"""
* with the "continue" statement we can stop the current iteration, and continue with the next

example
- continue to the next iteration if "i" is 3
"""
print("\n")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)



# the else statement
"""
* with the "else" statement we can run a block of code once when the condition no longer is true 

NOTE: the "else" block will NOT be executed if the loop is stopped by a "break" statement

example
- print a message once the condition is false
"""
print("\n")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


































