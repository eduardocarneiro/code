# python - iterators 



# python iterators
"""
* an iterator is an object that contains a countable number of values

* an iterator is an object that can be iterated upon, meaning that you can traverse through all the values 

* technically, in python, an iterator is an object which implements the iterator protocol, which consist of the methods __inter__()
and __next__()
"""



# iterator vs iterable
"""
* list, tuples, dictionaries and sets are all iterable objects. they  are iterable containers which you can get an iterator from

* all these objects have a iter() method which is used to get an iterator 

example:
- return an iterator from a tuple, and print each value 
"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


"""
* even strings are iterable objects, and can return an iterator

example:
- strings are also iterable objects, containing a sequence of characters 
"""
print("\n")

mystr = "banana"
myit = iter(mystr)

for i in range(6):
    print(next(myit))



# looping though an iterator
"""
* we can also use a "for" loop to iterate through an iterable object 

example:
- iterable the values of a tuple 
"""
mytuple = ("apple", "banana", "cherry")

for i in mytuple:
    print(i)


"""
example:
- iterable the characters of a string 
"""
mystr = "banana"

for i in mystr:
    print(i)


"""
NOTE: the "for" loop actually creates an iterator object and executes the "next()" method for each loop 
"""



# create an iterator 
"""
* to create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object

* as you will learn in the "Python Classes/Objects" chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created 

* the __iter__() method acts similiar, you can do operations (initializin etc.), but must always return the iterator object itself 

* the __next__() method also allows you to do operations, and must return the next item in the sequence 

example:
- create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returing 1,2,3,4,5 etc)
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



# stopIteration
"""
* the example above would continue forever if you had enough next() statements, or if it was used in a "for" loop 

* to prevent the iteration from going on forever, we can use the "stopIteration" statement 

* in the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times 

example:
- stop after 20 iterations 
"""
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers2()
myiter = iter(myclass)

for x in myiter:
    print(x)


