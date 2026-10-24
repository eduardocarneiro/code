# python - copy dictionaries


# copy a dictionary
"""
* you cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically be made in dict2

* tere are ways to make a copy, one way it to use the built-in dictionary method copy()

example
- make a copy of a dictionary with the copy() method 
"""
car1 = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}

copy_car1 = car1.copy()
print(copy_car1)


"""
* another way to make a copy is to use the built-in function dict()

example 
- make a copy of a dictionary with the dict() function 
"""
car2 = {
    "brand": "agrale",
    "model": "marrua",
    "year": 2026
}

copy_car2 = dict(car2)
print(copy_car2)
