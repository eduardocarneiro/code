# python - for loops
"""
* a "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

* this is less like "for" keyword in other programming language, and works more like an iterator method as found in other object-orientated programming languages

* with the "for" loop we can execute a set of statements, once for each item in a list, tuple, set etc 

NOTE: the "for" loop does not require an indexing variable to set beforehand

example 
- print each fruit in a fruit list 
"""

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)



# looping through a "string"
"""
* even strings are iterable objects, they contain a sequence of characters

example
- loop through the letters in the word "banana"
"""

for i in "banana":
    print(i)



# the break statement 
"""
* with the "break" statement we can stop the loop before it has looped through all the items 

example 
- exit the loop when x is "banana"
"""
print("\n")

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)
    if i == "banana":
        break



"""
example
- exit the loop when "x" is "banana", but this time the break comes before the print 
"""
print("\n")

fruits = ["orange", "mango", "banana", "cherry", "kiwi"]
print(fruits)

for i in fruits:
    if i == "banana":
        break
    print(i)



# the continue statement 
"""
* with the "continue" statement we can stop the current iteration of the loop, and continue with the next

example
- do not print banana
"""
print("\n")

fruits = ["apple", "banana", "cherry"]
print(fruits)

for i in fruits:
    if i == "banana":
        continue
    print(i)



# the range() function
"""
* to loop through a set of code a specified number of times, we can use range() function 

* the range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number 


NOTE: that range(6) is not the values of 0 to 6, but the values 0 to 5

example
- using the range() funcion 
"""
print("\n")
for i in range(6):
    print(i)



"""
* the range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)

example
- using the start parameter
"""
print("\n")
for i in range(2, 6):
    print(i)


"""
* the range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)

example
- increment sequence with 3 (default is 1)
"""
print("\n")
for i in range(1, 29, 2):
    print(i)



# else in for loop 
"""
* the "else", keyword in a "for" loop specifies a block of code to be executed when the loop is finished

example
- print all numbers from 0 to 5, and print a message when he loop has ended
"""
print("\n")

for i in range(1, 7):
    print(i)
else:
    print("finally finished")


"""
NOTE: the "else" block will NOT be executed if the loop is stopped by a "break" statement 

example:
- break the loop when "x" is 3, and see what happens with the "else" block 
"""

print("\n")
for i in range(6):
    if i == 3:
        break
    print(i)
else:
    print("finally finished")



# nested loops
"""
* a nested loop is a loop inside a loop 

* the "inner loop" will be executed one time for each iteration of the "outer loop"

example 
- print each adjective for every fruit 
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for b in fruits:
        print(a, b)



# the pass statement
"""
* "for" loops cannot be empty, but if you for some reason have a "for" loop with no content, put in the "pass" statement to avoid getting an error

example
"""
for i in [0, 1, 2]:
    pass

