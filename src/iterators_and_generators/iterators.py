# Iterators
# What is an Iterator?
# An iterator is an object that can be iterated upon, meaning you can traverse through all the values.
# Technically, an iterator is an object which implements the iterator protocol, which consists of the methods __iter__() and __next__().
#
# Creating an Iterator
# To create an iterator in Python, we use the following steps:
#
# Implement the __iter__() method, which returns the iterator object itself.
# Implement the __next__() method, which returns the next item from the sequence.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for num in my_iter:
    print(num)
    
    
# When to Use Which?
# Use iterators when you need full control over the iteration process and potentially more complex state management.
# Use generators when you need a simple and memory-efficient way to generate sequences of values on the fly.