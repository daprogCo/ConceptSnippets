"""
### Example of a simple decorator pattern in Python ###

A decorator or wrapper is a structural design pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects. It provides a flexible alternative to subclassing for extending functionality.

In Python, decorators are functions that take another function as an argument and return a new function that adds some kind of behavior to the original function. Decorators are typically used to modify the behavior of functions or methods without changing their source code. 

Some common use cases for decorators include logging, timing, and caching as getters(@property) and setters(@<attribute>.setter).
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Should print:
# -> "Something is happening before the function is called."
# -> "Hello"
# -> "Something is happening after the function is called."