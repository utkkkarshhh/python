# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# def myDecorator(func):
#   def wrapper():
#       print("Something is happening before the function is called.")
#       func()
#       print("Something is happening after the function is called.")
#   return wrapper
  
  
# def say_hello():
#     print("Hello")
  
# decoratedFunction = myDecorator(say_hello)
# decoratedFunction()



def newDecoratedFunction(func):
  def wrapper(*args, **kwargs):
      x = lambda a, b: a * b 
      print(f"Lambda Results: {x(2, 3)}")
      func(*args, **kwargs)
      print("First Lambda Result, then the argument vala function")
  return wrapper

# Frist Approach -> Call the inner function 
# def myWorld():
#   print("Welcome to my world!")
  
# z = newDecoratedFunction(myWorld)
# z()

# Second Approach
@newDecoratedFunction
def fun(name):
    print(f"This decorated function written by {name}")
    
fun("Utkarsh")
  

    