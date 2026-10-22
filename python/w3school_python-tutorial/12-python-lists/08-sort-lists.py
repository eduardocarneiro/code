# python - sort lists 

# sort list alphanumerically 
"""
* list objects have a sort() method that will sort the list alphanumerically, ascending, by default

example
- sort the list alphabetically 
"""
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(f"list1 before 'sort': ", list1)
list1.sort()
print(f"list1 after 'sort':  ", list1)


"""
example 
- sort the list numerically
"""
list2 = [45, 23, 67, 100, 1, 3, 25, 83, 72]
print(f"list2 before 'sort': ", list2)
list2.sort()
print(f"list2 after 'sort': ", list2)



# sort descending
"""
* to sort descending, use the keyword argument "reverse = True"

example
- sort the list descending
"""
list3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(f"list3 before 'sort descending': ", list3)
list3.sort(reverse = True)
print(f"list3 after 'sort descending': ", list3)


"""
example 
- sort the list descending numerically
"""
list4 = [4, 56, 23, 87, 100, 34, 3432, 3, 1, 78, 91, 45, 65]
print(f"list4 before 'sort descending numerically': ", list4)
list4.sort(reverse=True)
print(f"list4 after 'sort descending numerically': ", list4)



# customize sort function
"""
* you can also customize your own function by using the keyword argument "key = function"
* the function will return a number that will be used to sort the list (the lowest number first)

example 
- sort the list based on how close the number is to 50
"""
def myfunc(n):
    return abs(n - 50)

list5 = [100, 50, 65, 82, 23]
print(f"list5 before 'custom sort': ", list5)
list5.sort(key=myfunc)
print(f"list5 after 'custom sort': ", list5)



# case insensitive sort 
"""
* by default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters 

example 
- case sensitive sorting can give an unexpected result
"""
list6 = ["banana", "Orange", "kiwi", "cherry"]
print(f"list6 before 'sort case sensitive:' ", list6)
list6.sort()
print(f"list6 after 'sort case sensitive: '", list6)


"""
* luckily we can use built-in functions as key functions when sorting a list 
* so if you want a case-insensitive sort function, use str.lower as a key function

example
- perform a case-insensitive sort of the list
"""
list7 = ["banana", "Orange", "kiwi", "cherry"]
print(f"list7 before 'sort case insensitive': ", list7)
list7.sort(key = str.lower)
print(f"list7 after 'sort case insensitive': ", list7)



# reverse order 
"""
* what if you want to reverse the order of a list, regardless of the alphabetically
* the reverse() method reverses the current sorting order of the elements

example
- reverse the order of the list items
"""
list8 = ["banana", "Orange", "Kiwi", "cherry"]
print(f"list8 before 'sort reverse()': ", list8)
list8.reverse()
print(f"list8 after 'sort reverse()': ", list8)




















