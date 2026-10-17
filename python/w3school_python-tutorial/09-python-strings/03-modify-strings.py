# python - modify strings
"""
* python has a set of built-in methods that you can use on strings
"""



# upper case
"""
sample
- the upper() method returns the string in upper case:
"""

a = "Hello, World!"
print(a.upper())



# lower case
"""
sample
- the lower() method returns the string in lower case
"""
b = "Hello, World!"
print(a.lower())



# remove whitespace
"""
* whitespace is the space before and/or after the actual text, and very often you want to remove this space

sample
- the strip() method removes any whitespace from the beginning or the end
"""
c = " Hello, World! "
print(c)
print(c.strip())



# replace string 
"""
sample
- the replace() method replaces a string with another string
"""
d = "Hello, World!"
print(d.replace("He", "Je"))



# split string
"""
* the split() method returns a list where the text between the specified separator becomes the list items

sample
- the slipt() method splits the string into substrings if it finds instances of the separator
"""
e = "Hello, World!"
print(a.split(","))



# string methods
"""
* String Methods reference: https://www.w3schools.com/python/python_ref_string.asp
"""








