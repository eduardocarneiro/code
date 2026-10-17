# strings
"""
* strings in python are surrounded by either quotation marks, or double quotation marks

'hello' is the same as "hello"

* you can display a string literal with the print() function
"""
print("hello")
print('hello')



# quotes inside quotes
"""
* you can use quotes inside a string, as long as they don't match the quotes surrounding the string 
"""

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



# assign string to a variable
"""
* assigning a string to a variable is done with the variable name followed by an equal sign and the string
"""

a = "hello"
print(a)



# multiline strings 
"""
* you can assign a multiline string to a variable by using three quotes 
* you can use three double quotes
"""

b = """ asb deddhe dhewodhew  dhweodhewu d dwhedhwe ddhewd hewd dhewdhwie 
deiuhdiewhde dhewhdiewdiewhdeiw dhewidhe dheiwu dhew dehwi 
dehdiwe  ewe dwe rterg"""
print(b)

c = ''' abc ert otr drjw khk'''
print(c)



# strings are arrays
"""
* string in python are arrays of unicode characters
* python does not have a character data type, a single character is simply a string with a length of 1
* square brackets can be used to access elements of the string

* to get the character at position 1 (remember that the first character has the position 0)
"""
d = "hello, world"
print(a[1])



# looping through a string
"""
* Since strings are arrays, we can loop through the characters in a string, with a "for" loop.
* loop through the letters in the word "banana"
"""

for i in "banana":
    print(i)



# string length
"""
* to get the length of a string, use the "len()" function

sample
- the len() function returns the length of a string
"""
e = "Hello, world!"
print(len(e))



# check string
"""
* check if "free" is present in the following text
"""

txt = "The best things in life are free!"
print("free" in txt)

"""
* use it in an "if" statement

sample
- print only if "free" is present
"""

txt2 = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")



# check if not
"""
* to check if a certain phrase or character is NOT present in a string, we can use the keyword "not in"

sample
- check if expensive is NOT present in the following text
"""

txt = "The best things in life are free!"
print("expensive" not in txt)


"""
* use it in an "if" statement

sample
- print only if "expensive" is NOT present
"""

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")









































































































