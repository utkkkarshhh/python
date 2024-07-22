thisdict = {
    "brand": "Ford",
    "model": "Icon",
    "year": 1999,
}

# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#
# Dictionaries are written with curly brackets, and have keys and values:

print(thisdict)

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # Duplicate values will overwrite existing values:
}
print(thisdict)

# Get Length
print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
thisdict2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Type of Dictionary
print(type(thisdict2))

# Dict constructor
thisdict3 = dict(name = "Utkarsh", age = 22, grade = 12, passStatus = True)
print(thisdict3)

# Accessing Items
x = thisdict3["passStatus"]
print(x)


x = thisdict3.keys() # Get Keys
y = thisdict3.values() #Get Values
print(x, y)


# Get Items
# Will return each item in a dictionary as tuples in a list
z = thisdict3.items()
print(z)

# Check if key exists
if "model" in thisdict:
    print("Yes, It exists!")