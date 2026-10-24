# python - access dictionary items


# accessing items 
"""
* you can access the items of a dictionary by referring to its key name, inside square brackets

example
- get the value of the "model" key 
"""
dict1 = {
    "brand": "mitisubishi",
    "model": "l200 triton",
    "year": 2015
}
print(dict1["model"])


"""
* there is also a method called "get()" that will give you the same result

example
- get the value of the "model" key 
"""
print(dict1.get("year"))



# get keys
"""
* the keys() method will return a list of all the keys in the dictionary

example
- get a list of the keys
"""
print(dict1.keys())


"""
* the list of the keys is a view of the dictionary, and see that the keys list gets updated as well
"""
car = {
    "brand": "mitisubishi",
    "model": "l200 triton",
    "year": 2015
}
print(f"car before: ", car)

car["color"] = "white"
print(f"car after: ", car)



# get values
"""
* the values() method will return a list of all the values in the dictionary

example
- get a list of the values 
"""
print(car.values())


"""
* the list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list 

example
- make a change in the original dictionary, and see that the values list gets updated as well 
"""

car1 = {
    "brand": "mitisubishi",
    "model": "l200 triton",
    "year": 2015 
}

x = car.values()

print(f"x before: ", x)

car["year"] = 2020
print(f"x after: ",x)



# get items
"""
* the "items()" method will return each item in a dictionary, as tuples in a list

example
- get a list of key:value pairs
"""
car2 = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "colors": ["while", "black"]
}

print(car2.items())



"""
* the returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list 

example
- make a change in the original dictionary, and see that the items list gets updated as well 
"""
car3 = {
    "brand": "volkswagen",
    "model": "fusca",
    "year": 1985
}

result_car3 = car3.items()
print(f"car3 before change: ", result_car3)

car3["year"] =  1990
print(f"car3 after change: ", result_car3)


"""
example 
- add a new item to the original dictionary, and see that the items list gets updated as well
"""
car4 = {
    "brand": "fiat",
    "model": "uno"
}

result_car4 = car4.items()

print(f"car4 before: ", result_car4)

car4["year"] = 2000

print(f"car4 after: ", result_car4)



# check if key exists
"""
* to determine if a specified key is present in a dictionary use the "in" keyword

example
- check if "model" is present in the dictionary
"""
car5 = {
    "brand": "toyota",
    "model": "hilux",
    "year": 2026
}

if "model" in car5:
    print("YES, 'model' is one of the key")























































































