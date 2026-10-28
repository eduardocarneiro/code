# python - recursion


# recursion 
"""
* recursion is when a function calls itself

* recursion is a common mathematical and programming concept. it means that a function calls itself. this has the benefit of meaning that you can loop through data to reach a result 

* the developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. however, when written correctly recursion can be very efficient and mathematically-elegant approach to programming

example
- a simple recursive function that counts down from 5 
"""
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)



# base caes and recursive caes
"""
* every recursive function must have two parts
    - a "base case"      - a condition that stops the recursion
    - a "recursive case" - the function calling itself with a modified argument 

* without a base case, the function would call itself forever, causing a stack overflow error 

NOTE: the base case is crucial. always make sure your recursive function has a condition that will eventually be met 

example:
- identifying base case and recursive case 
""" 
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))



# fibonacci sequence
"""
* the fibonacci sequence is a classic example where each number is the sum of the two preceding ones. the sequence starts with 0 and 1 

0,1,1,3,5,8,13, ...

* the sequence continues indefinitely, with each number being the sum of the two preceding ones 

* we can use recursion to find a specific number in the sequence 

example
- find the 7th number in the fibonacci sequence 
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



# recursion with lists
"""
* recursion can be used to process lists by handling one element at a time 

example:
- calculate the sum of all elements in a list 
"""
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


"""
example:
- find the maximum value in a list 
"""
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [2, 7, 2, 9, 1]
print(find_max(my_list))



# recursion depth limit 
"""
* python has a limit on how deep recursion can go. the default limit is usually around 1000 recursive calls

example:
- check the recursion limit 
"""
import sys 
print(sys.getrecursionlimit())


"""
* if you need deeper recursion, you can increase the limit, but be careful as this can cause crashes4

example:
"""
# import sys 
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


"""
* increasing the recursion limit should be done with caution. for every deep recursion, consider using iteration instead
"""








































