# python - remove dictionary items

# removing items
"""
* there are several methods to remove items from a dictionary 

example
- the pop() method removes the item with the specified key name
"""
car1 = {
    "brand": "suzuki",
    "model": "jimny",
    "year": 2015
}

print(f"car1 before remove: ", car1)

car1.pop("model")

print(f"car1 after remove: ", car1)


"""
example
- the popitem() method removes the last inserted item (in version before 3.7, a random item is removed instead)
"""
car2 = {
    "brand": "agrale",
    "model": "marrua",
    "year": 2018
}

print(f"car2 before popitem(): ", car2)

car2.popitem() 

print(f"car2 after popitem(): ", car2)


"""
example
- the "del" keyword removes the item with the specified key name 
"""

car3 = {
    "brand": "ford",
    "model": "ranger raptor",
    "year": 2026
}

print(f"car3 before: ", car3)

del car3["year"]

print(f"car3 after: ", car3)

"""
example
- the "del" keyword can also delete the dictionary completely
"""
car4 = {
    "brand": "chevrolet",
    "model": "celta",
    "year": 2011
}

del car4


"""
example
- the clear() method empties the dictionary 
"""
car5 = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}

print(car5)
car5.clear()
print(car5)




























