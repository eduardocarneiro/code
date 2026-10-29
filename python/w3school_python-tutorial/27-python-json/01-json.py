# python - json 
"""
* JSON is a syntax for storing and exchanging data 

* JSON is text, written with JavaScript object notation 
"""



# JSON in python 
"""
* python has a built-in package called "json", which can be used to work with JSON data 

example:
- import the json module 

 -------------
| import json |
 -------------

"""



# parse JSON - convert from JSON to python 
"""
* if you have a JSON string, you can parse it by using the "json.loads()" method 

NOTE: the result will be a Python Dictionary

example: 
- convert from JSON to python 
"""
import json 

# some JSON 
x = '{ "name": "EOC", "age": 30, "city": "São Paulo"}'

# parse x:
y = json.loads(x)

# the result is a python dictionay 
print(y["age"])



# convert from python to JSON 
"""
* if you have a python object, you can convert it into a JSON string by using the "json.dumps()" method 

example:
- convert from python to JSON 
"""
import json 

# a python object (dict)
x = {
    "name": "eoc",
    "age": 41,
    "country": "Brazil"
}

# convert into JSON 
y = json.dumps(x)
print(y)



"""
* you can convert python objects of the following types, into JSON strings 
    - dict 
    - list
    - tuple
    - string
    - int 
    - float
    - True 
    - False 
    - None 

example:
- convert python objects into JSON strings, and print the value 
"""
import json

print(json.dumps({"name": "eoc", "age": "41"}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


"""
* when you convert from python to JSON, python objects are converted into the JSON (JavaScript) equivalent 


 -----------------------
| python        JSON    |
| dict          object  |
| list          array   |
| tuple         array   |
| str           string  |
| int           number  |
| float         number  |
| True          true    |
| False         false   |
| None          null    |
 -----------------------

example 
- convert a python object containing all the legal data types 
"""
import json 

x = {
    "name": "eoc",
    "age": 41,
    "married": True,
    "divorced": False,
    "children": ("sarah"),
    "pets": ("joaquin", "benjamin", "natal", "sabrina"),
    "cars": [
        {"model": "mitisubishi", "mpg": 35.0},
        {"model": "nissan", "mpg": 24.1}
    ]
}

print(json.dumps(x))



# format the result
"""
* the example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks

* the "json.dumps() method has parameters to make it easier to read the result"

example:
- use the "indent" parameter to define the numbers of indents 
"""
print("\n")
print(json.dumps(x, indent=4))



""" 
* you can also define the separators, default value is (",",":"), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values 

example:
- use the "separators" parameter to change the default separator 
"""
print(json.dumps(x, indent=4, separators=(". ", " = ")))



# order the result 
"""
* the "json.dumps()" method has parameters to order the keys in the result

example:
- use the "sort_keys" parameter to specify if the result should be sorted or not 
"""
print(json.dumps(x, indent=4, sort_keys=True))



























































































