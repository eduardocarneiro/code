# python - lambda


# lambda functions
"""
* a lambda function is a small anonymous function 

* a lambda function can take any number of arguments, but can only have one expression 


syntax
 -------------------------------
| lambda arguments : expression |
 -------------------------------

The expression is executed and the result is returned 

example:
- add 10 to argument "a", and return the result 
"""
x = lambda a : a + 10
print(x(5))


"""
* lambda functions can take any number of arguments

example:
- multiply argument "a" with argument "b" and return the result 
"""
x = lambda a, b : a * b
print(x(5, 6))


"""
example:
- summarize argument "a", "b", and "c" and return the result 
"""
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))



# why use lambda functions
"""
* the power of lambda is better shown when you use them as an anonymous function inside another function 

* say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number 
"""
def fnc1(n):
    return lambda a : a * n


"""
* use that function definition to make a function that always doubles the number you send in 

example
"""
def fnc2(n):
    return lambda a : a * n

mydoubler = fnc2(2)

print(mydoubler(11))



"""
* or, use the same function definition to make a function that always triples the number you send in 

example 
"""
def fnc3(n):
    return lambda a : a * n 

mytripler  = fnc3(3)
print(mytripler(11))


"""
* or, use the same function definition to make both functions, in the same program 

example 
"""
def fnc4(n):
    return lambda a : a * n 

mydoubler = fnc4(2)
mytripler = fnc4(3)

print(mydoubler(11))
print(mytripler(11))

"""
* use lambda functions when an anonymous function is required for a short period of time 
"""



# lambda with built-in functions
"""
* lambda functions are commonly used with built-in functions like map(), filter(), and sorted() 
"""



# using lambda with map() 
"""
* the map() function applies a function to every item in an iterable

example 
- double all number in a list 
"""
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)



# using lambda with filter() 
"""
* the filter() function creates a list of items for which a function returns True 

example:
- filter out odd numbers from a list 
"""
numbers = [1, 2, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)



# using lambda with sorted() 
"""
* the sorted() function can use a lambda as a key for custom sorting

example:
- sort a list of tuples by the seond element 
"""
students = [("emil", 25), ("tobias", 22), ("linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)



"""
example:
- sort strings by length
"""
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

























































