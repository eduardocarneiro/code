# python - arrays 
"""
NOTE: python does not have built-in support for Arrays, but python lists can be used instead 
"""



# arrays 
"""
NOTE: this page shows you how to use "lists" are "arrays", however, to work with arrays in python you will have to import a library, like the "numpy library - https://www.w3schools.com/python/numpy/default.asp "

* arrays are used to store multiple values in on single variable

example:
- create an array containing car names 
"""
cars = ["ford", "volvo", "bmw"]



# what is an array
"""
* an array is a special variable, which can hold more than one value at a time 

* if you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

 ----------------
| car1 = "ford"  |
| car2 = "volvo" |
| car3 = "bmw"   |
 ---------------- 

 * however, what if you want to loop through the cars and find a specific one? and what if you had not 3 cars, but 300?

 * the solution is an array 

 * an array can hold many values under a single name, and you can access the values by referring to an index number 
"""



# access the elements of an array
"""
* you refer to an array element by referring to the index number

example:
- get the value of the first array item 
"""
x = cars[0]
print(x)

"""
example:
- modify the value of the first array item 
"""
cars[0] = "toyota"
print(cars)



# the length of an array
"""
* use the len() method to return the length of an array (the number of elements in an array)

NOTE: the length of an array is always one more than the highest array index 

example:
- return the number of elements in the "cars" array 
"""
x = len(cars)
print(x)



# looping array elements
"""
* you can use the "for in" loop to loop through all the elements of an array 

example:
- print each item in the "cars" array
"""
for i in cars:
    print(i)



# adding array elements
"""
* you can use the append() method to add an element to an array 

example:
- add one more element to the "cars" array 
"""
cars.append("honda")
print(cars)




# removing array elements
"""
* you can use the pop(). method to remove an element from the array

example:
- delete the second element of the cars array 
"""
print("\n")
print(cars)
cars.pop(1)
print(cars)

"""
* you can also use the "remove()" method to remove an element from the array 

example:
- delete the element that has the value "volvo"
"""
cars.append("Volvo")
print(cars)

cars.remove("Volvo")
print(cars)


"""
NOTE: the list's "remove()" method only removes the first occurrence of the specified value 
"""



# array methods 
"""
* python has a set of built-in methods that you can use on lists/arrays 



 ---------------------------------------------------------------------------------------------
| method        description                                                                   |
| append()      adds an element at the end of the list                                        |
| clear()       removes all the elements from the list                                        |
| copy()        returns a copy of the list                                                    |
| count()       returns the number of elements with the specified value                       |
| extend()      add the elements of a list (or any iterable), to the end of the current list  |
| index()       returns the index of the first element with the specified value               |
| insert()      adds an element at the specified position                                     |
| pop()         removes the element at the specified position                                 |
| remove()      removes the first item with the specified value                               |
| reverse()     reverses the order of the list                                                |
| sort()        sorts the list                                                                |
 ---------------------------------------------------------------------------------------------


NOTE: python does not have built-in support for arrays, but python lists can be used instead 
"""










































