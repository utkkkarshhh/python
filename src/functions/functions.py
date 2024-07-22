# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a function:
def my_function(a):
    print("Hello World "+ str(a))

my_function(2)


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def multiple_args(*names):
    for x in names:
        print(x)

multiple_args(1, 2, 3);


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def keyword_arguments(child1, child2, child3):
    return "The youngest child is " + child3

print(keyword_arguments(child1 = "Samar", child2 = "Sohan", child3 = "Chintu"))


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def arb_keyword_arguments(**kargs):
    print("His last name is " + kargs["lastName"])

arb_keyword_arguments(fNnme = "Utkarsh", lastName = "Bhardwaj")


# Default Parameter Value
# If we call the function without argument, it uses the default value:

def country(name = "India"):
    print("He is from " + name)

country("USA")
country()
country("Brazil")

# We can pass list as an argument too
# Use pass statement is cases you want to do nothing

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def function1(x, /):
    print(x)

function1(2);

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def function2(*, x):
  print (x)
  
function2(x = 2)

# Recursion
def recursion(k):
    if(k > 0):
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result

recursion(6)
