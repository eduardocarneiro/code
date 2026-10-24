# python frozenset


# python frozenset
"""
* frozenset is an immutable version of a set

* like "sets", it contains unique, unordered, unchangeable elements

* unlike "sets", elements cannot be added or removed from a frozenset 
"""



# creating a frozenset
"""
* use the "frozenset()" constructor to create a frozenset from any iterable

example 
- create a frozenset and check its type
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))



# frozenset methods
"""
* being immutable means you cannot add or remove elements. however, frozensets support all non-mutating operations of sets


 ----------------------------------------------------------------------------------------------------------
| method                    shortcut    description                                                        |
| copy()                                returns a shallow copy                                             |
| difference()              -           returns a new frozenset with the difference                        |
| intersection()            &           returns a new frozenset with the intersection                      |
| isdisjoint()                          returns True if there is NO intersection between two frozensets    |
| issubset()                <= / <      returns True if this frozenset is a (proper) subset of another     |
| issuperset()              >= / >      returns True if this frozenset is a (proper) superset of another   |
| symmetric_difference()    ^           returns a new frozenset with the symmetric differences             |
| union()                   |           returns a new frozenset containing the union                       |
 ----------------------------------------------------------------------------------------------------------
"""
