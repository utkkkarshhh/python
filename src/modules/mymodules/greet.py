def myAdditionFunction(function):
    def wrapper(*args, **kwargs): 
        print("Adding two numbers here: ")
        function(*args, **kwargs)
        print("You can see the result above")
    return wrapper

@myAdditionFunction
def addProduct(a, b):
    print(f"Result of addition is {a + b}")


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}