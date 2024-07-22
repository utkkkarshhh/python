# List
""" 
JS Equivalent: Array
1. Lists are ordered, changeable (mutable), and allow duplicate elements.
2. Defined using square brackets [].
"""
myList = [1, 2, 3, 4, 5]
print(myList[2])
myList.append(6)  # Appending to the list
myList.remove(5)  # Remove element with value 5
print(myList[1:3])  # Slicing the list from index 1 to 2

print(myList)


# Tuples
""" 
JS Equivalent: Not directly available, but can use arrays with Object.freeze() to make them immutable
1. Tuples are ordered, unchangeable, and allow duplicate elements.
2. Defined using parentheses ().
"""

myTuple = (1, 2, 3, 4, 5)
print(myTuple[1])  # Accessing the nth index


# Sets
""" 
JS Equivalent: Set
1. Sets are unordered, unchangeable (but can add or remove items), and do not allow duplicate elements.
2. Defined using curly braces {} or the set() constructor.
"""

mySet = {1, 2, 3, 4, 5}
mySet.add(6)  # Adding to the set
mySet.remove(3)  # Removing from the set
print(mySet)


# Dictionaries
""" 
JS Equivalent: Object or Map
1. Dictionaries are unordered, changeable (mutable), and do not allow duplicate keys.
2. Defined using curly braces {} with key-value pairs.
"""

myDict = {'a': 1, 'b': 2, 'c': 3}
print(myDict['a'])  # Accessing value by key
myDict['d'] = 4  # Adding a key-value pair
print(myDict)


# Arrays
""" 
JS Equivalent: Not available natively in Python.
1. Used for numerical operations where elements are of the same type.
2. Typically handled in Python using the array module or NumPy library.
3. NumPy arrays are more efficient for large numerical computations.
"""

import array as arr

myArray = arr.array('i', [1, 2, 3, 4, 5])
print(myArray[2])


