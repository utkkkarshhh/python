# Looping through a list
fruits = ["apple", "banana" , "cherry"]
for x in fruits:
    print(x)


# Looping through a string
for x in "banana":
    print(x)

# Break statement
fruits = ["apple", "banana" , "cherry"]
for x in fruits:
    print(x)
    if(x == "banana"):
        break


# Else block does not get executed if the loop is stopped by a break statement

for x in fruits:
    if(x == "banana"):
        break
    else:
        print(x)
else:
    print("Loop completed")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if(x != "apple"):
        continue
    print(x)

# Range Function
for x in range(6):
    print(x) #Prints from 0-5

for x in range(2, 4):
    print(x)

# Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally Finished")


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

""" Output
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""

# The pass statement
for x in [0, 1, 2]:
    pass