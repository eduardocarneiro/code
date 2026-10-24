# python - join sets


# join sets
"""
* there are several ways to join two or more sets in python 

    - the "union()" and "update()" methods joins all items from both sets 
    - the "intersection()" method keeps ONLY the duplicates
    - the "difference()" method keeps the items from the first set that are not in the other set(s)
    - the "symmetric_difference()" method keeps all items EXCEPT the duplicates
"""



# union
"""
* the "union()" method returns a new set with all items from both sets 

example 
- join set1 and set2 into a new set 
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

"""
* you can use the "|" operator instead of the "union()" method and you will get the same result

example
- use | to join two sets 
"""
set4 = {"apple", "banana", "cherry"}
set5 = {1, 2, 3}

set6 = set4 | set5
print(set6)



# join multiple sets
"""
* all the joining methods and operators can be used to join multiple sets 
* when using a method, just add more sets in the parentheses, separated by commas

example
- join multiple sets with the "union()" method
"""
set7 = {1, 2, 3}
set8 = {"a", "b", "d"}
set9 = {"orange", "mango", "kiwi"}
set10 = {"Eduardo", "Sarah", "Natty"}

set_result = set7.union(set8, set9, set10)
print(set_result)


"""
* when using the | operator, separate the sets with more | operators

example 
- use | to join two sets 
"""
set_result2 = set7 | set8 | set9 | set10
print(set_result2)




# join a set and a tuple 
"""
* the "union()" method allows you to join a set with other data types, like lists or tuples

* the result will be a "set"


NOTE: the "|" operator only allows you to join sets with sets, and not with other data types like you can with the "union()" method 

example 
- join a set with a tuple 
"""
set11 = {"a", "b", "c"}
print(f"set11: ", set11)
print(type(set11))

tuple1 = (1, 2, 3)
print(f"tuple1: ", tuple1)
print(type(tuple1))

set_result3 = set1.union(tuple1)
print(set_result3)
print(type(set_result3))



# update 
"""
* the "update()" method inserts all items from one set into another

* the "update()" changes the original set, and does not return a new set 

NOTE: both "union()" and "update()" will exclude any duplicate items 

example
- the "update()" method inserts the items in set13 into set12 
"""
set12 = {"a", "b", "c"}
set13 = {1, 2, 3}

set12.update(set13)
print(set12)



# intersection

"""
* keep ONLY the duplicates

* the "intersectin()" method will return a new set, that only contains the items that are present in both sets 

example
- join set14 and set15, but keep only the duplicates 
"""
set14 = {"apple", "banana", "orange"}
print(f"set14: ", set14)

set15 = {"banana", "kiwi", "apple", "mango", "pineapple", "cherry"}
print(f"set15: ", set15)

set_result4 = set14.intersection(set15)
print(set_result4)


"""
* you can use the "&" operator instead of the "intersection()" method, and yuo will get the same result 


NOTE: the "&" operator only allows you to join sets with sets, and not with other data types like you can with the "intersection()" method

example
- use "&" to join two sets 
"""
set16 = {"apple", "abc", "banana"} 
print(f"set16: ", set16)
set17 = {"abc", "def", "ghi"}
print(f"set17: ", set17)

set_result5 = set16 & set17
print(set_result5)


"""
* the "intersection_update()" method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set 

example
- keep the items that exist in both "set18" and "set19"
"""
set18 = {"apple", "banana", "orange"}
set19 = {"banana", "abc", "a"}

set18.intersection_update(set19)
print(set18)


"""
* the values "True" and 1 are considered the same value. The same goes for "False" and 0

example
- join sets that contains the values "True", "False", 1, and 0, and see what is considered as duplicates 
"""
set20 = {"apple", 1, "banana", 0, "cherry", True}
set21 = {False, "google", 1, "apple", 2, True}

set_result6 = set20.intersection(set21)
print(set_result6)



# difference
"""
* the "difference()" method will return a new set that will contain only the items from the first set that are not present in the other set 

example
- keep all items from set22 that are not in set23
"""
set22 = {"a", "b", 1}
print(f"set22", set22)
set23 = {"abc", 1, 2, 3, "apple"}
print(f"set23", set23)

set_result7 = set22.difference(set23)
print(set_result7)


"""
* you can use the "-" operator instead of the "difference()" method, and you will get the same result 

NOTE: the "-" operator only allows you to join sets with sets, and not with other data types like you can with the difference() method 

example
- use "-" to join two sets 
"""
set24 = {"apple", "banana", "cherry"}
print(f"set24", set24)
set25 = {"abc", 1, "cherry"}
print(f"set25", set25)

set_result8 = set24 - set25
print(set_result8)


"""
* the "difference_update()" method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set

example
* use the "difference_update()" method to keep only the items from the first set that are not present in the other set
"""
set26 = {1, 2, 3}
print(f"set26: ", set26)
set27 = {1, "abc", "orange"}
print(f"set27: ", set27)

set26.difference_update(set27)
print(set26)



# symmetric differences 

"""
* the "symmetric_difference()" method will keep only the elements that are NOT present in both sets 

example 
- keep the items that are not present in both sets 
"""
set28 = {"a", "b", "d"}
print(f"set28: ", set28)
set29 = {"orange", 1, "a", 234, "appple", "b"}
print(f"set29: ", set29)

set_result9 = set28.symmetric_difference(set29)
print(set_result9)


"""
* you can use the "^" operator instead of the "symmetric_difference()" method, and you will get the same result 


NOTE: the "^" operator only allows you to join sets with sets, and not with other data types, like you can with the "symmetric_difference()" method


example 
- use "^" to join two sets 
"""
set30 = {"apple", "banana", "cherry"}
print(f"set30: ", set30)
set31 = {"google", "microsoft", "apple"}
print(f"set31: ", set31)

set_result10 = set30 ^ set31
print(set_result10)


"""
* the "symmetric_difference_update()" method will also keep all the duplicates, but it will change the original set instead of returning a new set 

example 
- user the "symmetric_difference_update()" method to keep the items that are not present in both sets 
"""
set32 = {"apple", "banana", "cherry"}
print(f"set32: ", set32)
set33 = {"google", "oracle", "apple"}
print(f"set33: ", set33)

set32.symmetric_difference_update(set33)
print(set32)



































































































