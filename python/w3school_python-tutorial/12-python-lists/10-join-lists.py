# python - join lists

# join two lists 
"""
* there are several ways to join, or concatenate, two or more lists in python 
* one of the easiest ways are by using the + operator

example 
- join two list 
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


"""
* another way to join two lists is by appending all the items from list3 into list4, one by one

example
- append list4 into list3 
"""
list3 = ["a", "b", "c"]
print(f"list3 before 'append()': ", list3)
list4 = [1, 2, 3]
print(f"list4 before 'append()': ", list4)

for i in list2:
    list1.append(i)

print(f"list1 after 'append()': ", list1)


"""
* or you can use the extend() method, where the purpose is to add elements from one list to another list 

example
- use the extend() method to add list6 to list5
"""
list5 = ["a", "b", "c"]
print(f"list5 before 'extend()': ", list5)
list6 = [1, 2, 3]
print(f"list6 before 'extend()': ", list6)
list5.extend(list6)
print(f"list5 after 'extend()': ", list5)

