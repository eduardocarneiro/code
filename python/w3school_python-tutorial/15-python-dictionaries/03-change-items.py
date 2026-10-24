# python - change dictionary items

# change values
"""
* you can change the value of a specific item by referring to its key name

example 
- change the "year" to 2018
"""
car1 = {
    "brand": "fiat",
    "model": "uno",
    "year": 2000
}

print(f"car1 before: ", car1)

car1["year"] = 2018 
print(f"car1 after: ", car1)



# update dictionary
"""
* the "update()" method will update the dictionary with the items from the given argument

* the argument must be a dictionary, or an iterable object with key:value pairs

example 
- update the "year" of the car by using the update() method 
"""
car2 = {
    "brand": "chevrolet",
    "model": "onix",
    "year": 2014
}

car2.update({"year": 2020})
print(car2)
car2.update({"brand":"ford", "model":"focus"})
print(car2)























