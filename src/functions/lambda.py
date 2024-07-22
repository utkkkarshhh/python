# Lambda Function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

x = lambda a, b: print(a + b)
x(10, 19)

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myFunction(n):
    return lambda a : a * n

multiplyWithFive = myFunction(5) 
print(multiplyWithFive(10)) 