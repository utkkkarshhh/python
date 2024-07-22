# List
# Lists are used to store multiple items in a single variable.
#
# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

# Creating a list
names = ["Utkarsh", "Ram", "Sohan"]

for name in names:
    print(name)

# List items are ordered, changeable and allow duplicate values

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

print(names) #Print the list
print(len(names)) #Prints the length of the list


list1 = ["Apple", "Banana", "Cherries"] #String List
list2 = [1, 2, 3, 4, 5] #Integer List
list3 = [True, False, False, True] #Boolean List

print(type(list1))

# The list constructor

# It is also possible to use the list() constructor when creating a new list.

thislist = list(("Apple", "Bananas", "Cherries"))
print(thislist)

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

