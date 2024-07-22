# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

#ORDERED and UNCHANGEABLE
#Tuples are indexed

thistuple = ("Apple", "Banana", "Cherries")
print(thistuple)

# Accessing using index
print(thistuple[0])

# Allows duplicates
newTuple = ("Apple", "Banana", "Cherries","Apple", "Banana", "Cherries")
print(newTuple)

# Get Length
print(len(newTuple))

# When creating tuple with only one item, make sure to add a comma after that in order for python to recognise it as a Tuple
sampleTuple1 = ("Apple" )
sampleTuple2 = ("Apple", )
print(type(sampleTuple1))
print(type(sampleTuple2))

# Multiple Data Types in Tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Tuple constructor
thisTuple = tuple(("Apple", "Banana"))
print(thisTuple)

