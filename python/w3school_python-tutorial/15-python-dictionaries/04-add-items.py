# python - add dictionary items

# adding items
"""
* adding an item to the dictinary is done by using a new index key and assigning a value to it 

example
"""
car1 = {
    "brand": "agrale",
    "model": "marrua",
    "year": 2014
}
print(f"car1 before: ", car1)

car1["color"] = "white"

print(f"car1 after: ", car1)



# update dictionary
"""
* the update() method will update the dictionary with the items from a given argument. if the item does not exist, the item will be added 

* the argument must be a dictionary or an iterable object with key:value pairs

example
- add a color item to the dictionary by using the update() method 
"""
car2 = {
    "brand": "mitisubishi",
    "model": "tr4",
    "year": 2018
}
print(f"car2 before: ", car2)

car2.update({"brand":"suzuki"})
print(f"car2 after 1 update: ", car2)

car2.update({"brand": "troller", "model": "tr4", "year": 2015})
print(f"car2 after 2 change: ", car2)

