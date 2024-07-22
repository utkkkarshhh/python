# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

try:
    print(x)
except:
    print("An exception has occurred")


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


try:
    print("Hello")
except:
    print("An exception occurred")
else: 
    print("No errors occurred")


try:
    print(x)
except: 
    print("An exception occurred")
finally: 
    print("This code has finished")

try:
    f = open("demofile.txt", "w")
    try:
        f.write("Lorem ipsum dolor")
    except Exception as e: 
        print(f"Something went wrong when writing to the file: {e}")
    finally:
        f.close()
except Exception as e: 
    print(f"Something went wrong when opening the file: {e}")