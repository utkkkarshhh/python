# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


from mymodules import greet #From particular folder import this file
from mymodules import greet as g #From particular folder import this file with this name

g.addProduct(2, 5)

print(greet.person1["name"])