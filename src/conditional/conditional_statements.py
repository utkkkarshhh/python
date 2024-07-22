# If...Else
"""
a == b #A is equal to B
a != b #A is not equal to B
a < b  #A is smaller than B
a <= b #A is smaller than equal to B
a > b #A is greater than B
a >= b  #A is greater than equal to B
"""

a = 31
b = 30

if a > b: 
    print("A is greater than B")
elif a == b:
    print("A is equal to B")
else:
    print("B is greater than A")


# Short hand If(For only one condition)
if a > b: print("A is greater than B")

# Short hand if/else
print("A is greater than B") if a > b else print("B is greater than A")

# "or" and "and"
a = 200
b = 33
c = 500
if a > b or a > c:
    print("Atleast one is true")


a = 200
b = 33
c = 500
if a > b and a > c:
    print("Both conditions are true")
else:
    print("One condition is false")


# Not
a = 33
b = 200
if not a > b:
    print("A is not greater than B")

# NestedIf

x = 41
if(x > 10):
    print("X is greater than 10")
    if(x > 20):
        print("X is also greater than 20")
    else:
        print("But not above 20")

# Pass
if x > 4:
    pass







