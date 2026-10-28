# python - range 



# python range
"""
* the built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times 

* this set of numbers has its own data type called "range"

NOTE: immutable means that it cannot be modified after it is created 
"""



# creating ranges
"""
* the range() function can be called with 1,2 or 3 arguments, using this syntax 

 --------------------------
| range(start, stop, step) |
 --------------------------
"""



# call range() with one arguments
"""
* if the range function is called with only one argument, the argument represents the "stop" value 

* the "start" argument is optional, and if not provided, it defaults to 0 

* "range(10)" returns a sequence of each number from 0 to 9. (the start argument, 0 is inclusive, and the stop argument, 10 is exclusive)

example:
- create a range of numbers from 0 to 9
"""
x = range(10)
print(x)
print(type(x))


# call range() with two arguments 
"""
* if the range function is called with two arguments, the first argument represents the "start" value, and the second argument represents the "stop" value 

* "range(3, 10) returns a sequence of each number from 3 to 9"

example:
- create a range of numbers from 3 to 9
"""
x = range(3, 10)
print(x)



# call range() with three arguments 
"""
* if the range function is called with three arguments, the third argument represents the "step" value 

* the step value means the difference between each number in the sequence. it is optional, and if not provided, it defaults to 1

* "range(3, 10, 2)" returns a sequence of each number from 3 to 9, with a step of 2

example:
- create a range of numbers from 3 to 9
"""
x = range(3, 10, 2)
print(x)



# using ranges 
"""
* ranges are often used in "for" loops to iterate over a sequence of numbers 

example:
- iterate over each value in a range 
"""
for i in range(10):
    print(i)



# using list to display ranges
"""
* the range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable 

* therefore, ranges are often converted to lists for display 

example:
- convert different ranges to list 
"""
print("\n")
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))


# slicing ranges
"""
* like other sequences, ranges can be sliced to extract a subsequence 

NOTE: the first print statement returns the value at index 2, and the second print statement returns a new range object, from index 0 to 3

example:
- extract a subsequence from a range 
"""
r = range(10)
print(r[2])
print(r[:3])



# membership testing
"""
* ranges support membership testing with the "in" operator 

NOTE: the return value is True when the number is present in the range, and False whnen it is not

example:
- test if the numbers 6 and 7 are present in a range 
"""
r = range(0, 10, 2)
print(6 in r)
print(7 in r)



# length 
"""
* ranges support the len() function to get the number of elements in the range 

example:
- get the length of a range 
"""
r = range(0, 10, 2)
print(len(r))


















