# Generators
# What is a Generator?
# Generators are a simple way of creating iterators using a function rather than a class. 
# They use the yield keyword to return values one at a time, suspending the function’s state between each.

# Creating a Generator
# To create a generator, you define a function as usual but use the yield keyword to return data.


def my_generator():
    x = 1
    while x <= 5: 
        yield x
        x += 1
        
gen = my_generator()

for num in gen:
    print(num)