# python - nested dictionaries


# nested dictionaries 
"""
* a dictionary can contain dictionaries, this is called nested dictionaries

example
- create a dictionary that contain three dictionaries 
"""
myfamily = {
    "child1": {
        "name": "emil",
        "year": 5
    },
    "child2": {
        "name": "tobias",
        "year": 7
    },
    "child3": {
        "name": "linux",
        "year": 2
    }
}

print(myfamily)


"""
* if you want to add three dictionaries into a new dictionary 

example  
- create three dictionaries, then create one dictionary that will contain the other three dictionaries 
"""

person1 = {
    "name": "Sarah",
    "age": 7
},
person2 = {
    "name": "Dezenatty",
    "age": 39
},
person3 = {
    "name": "Eduardo",
    "age": 41
}

myfamily2 = {
    "person1": person1,
    "person2": person2,
    "person3": person3
}
print(myfamily2)



# access items in nested dictionaries
"""
* to access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary 

example
- print the name of child person2 
"""
print("\n")
print(f"myfamily 'child2' 'name': ", myfamily)
print(myfamily["child2"]["name"])



# loop through nested dictionaries 
"""
* you can loop through a dictionary by using the items() method like this 

example
- loop through the keys and values of all nested dictionaries
"""

for key, value in myfamily.items():
    print(key)
    for i in value:
        print(i + ":", value[i])


# explanation about the code above:
"""
1. The Data Structure (myfamily)

The variable myfamily is a dictionary that contains three keys: "child1", "child2", and "child3".

    - The value of each key is another dictionary containing details ("name" and "year") about a child.

2. The Outer Loop (for x, obj in myfamily.items():)

    - .items(): This method returns a list of key-value pairs from the dictionary.

    - x: Captures the key of the outer dictionary (e.g., "child1", "child2", "child3").

    - obj: Captures the value of the outer dictionary, which in this case is the inner dictionary itself (e.g., {"name": "Emil", "year": 2004}).

When the outer loop runs:

    - It first prints x (child1).

    - Then, it enters the inner loop for that specific child's dictionary (obj).

3. The Inner Loop (for y in obj:)

    - y: Loops through the keys of the inner dictionary ("name" and then "year").

    - obj[y]: Accesses the value associated with that inner key (e.g., obj["name"] evaluates to "Emil", and obj["year"] evaluates to 2004).

    - print(y + ':', obj[y]): Concatenates and prints the key and its value (e.g., name: Emil).

Expected Output

When you run this code in your terminal, the output will look like this:
Plaintext

child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011

Summary

    - Outer loop: Iterates through the main dictionary to grab each child's identifier (child1, child2, etc.) and their respective dictionaries.

    - Inner loop: Digs inside each child's dictionary to print out their individual attributes (name and year).

"""


