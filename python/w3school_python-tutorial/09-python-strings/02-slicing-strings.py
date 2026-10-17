# slicing
"""
* you can return a range of characters by using the slice syntax
* specify the start index and the end index, separated by a colon, to return a part of the string

sample
- get the characters from position 2 to position 5 (not included)
"""
a = "Hello, World!"
print(a[0:5])



# slice from the start
"""
* by leaving out the start index, the range will start at the first characters
sample
- get the characters from the start to position 5 (not included)
"""
b = "Hello, World!"
print(b[:5])




# slice to the end
"""
* by leaving out the end index, the range will go to the end

sample
- get the characters from position 2, and all the way to the end
"""
c = "Hello, World!"
print(c[7:])




# negative indexing
"""
* use negative indexes to start the slice from the end of the string

sample
- get the characters:
 From: "o" in "World" (position -5)
 To, but not included: "d" in "World!" (position -2)
"""
d = "Hello, World!"
print(b[-6:-1])




