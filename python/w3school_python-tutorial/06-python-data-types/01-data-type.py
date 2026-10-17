# built-in data types
"""
* python has the following data types built-in by default, in these categories

 ________________________________________________
| text type:        str                          |
| numeric types:    int, float, complex          |
| sequence types:   list, tuple, range           |
| mapping type:     dict                         |
| set types:        set, frozenset               |
| boolean type:     bool                         |
| binary types:     bytes, bytearray, memoryview |
| none type:        NoneType                     |
 _________________________________________________
"""


# getting the data type
"""
* you can get the data type of any object by using the type() function
"""

x = 5
print(type(x))


# setting the data type 
"""
* in python the data type is set when you assign a value to a variable
"""
a = "hello world"                               # str
b = 20                                          # int
c = 20.5                                        # float
d = 1j                                          # complex
e = ["apple", "banana", "cherry"]               # list
f = ("apple", "banana", "cherry")               # tuple
g = range(6)                                    # range
h = {"name" : "John", "age" : 36}               # dict
i = {"apple", "banana", "cherry"}               # set
j = frozenset({"apple", "banana", "cherry"})    # frozenset
k = True                                        # bool 
l = b"Hello"                                    # bytes
m = bytearray(5)                                # bytearray
n = memoryview(bytes(5))                        # memoryview
o = None                                        # NoneType

for i in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]:
    print(i)
    print(type(i), end="\n\n")



# setting the specific data type
a = str("hello world")                          # str
b = int(20)                                     # int
c = float(20.5)                                 # float
d = complex(1j)                                 # complex
e = list(["apple", "banana", "cherry"])         # list
f = tuple(("apple", "banana", "cherry"))        # tuple
g = range(6)                                    # range
h = dict(name="John", age=36)                   # dict
i = set(("apple", "banana", "cherry"))          # set
j = frozenset(("apple", "banana", "cherry"))    # frozenset
k = bool(5)                                     # bool 
l = bytes(5)                                    # bytes
m = bytearray(5)                                # bytearray
n = memoryview(bytes(5))                        # memoryview

for i in [a, b, c, d, e, f, g, h, i, j, k, l, m, n]:
    print(i)
    print(type(i), end="\n\n")
