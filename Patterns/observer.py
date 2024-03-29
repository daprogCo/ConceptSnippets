"""
### Example of the observer pattern in Python ###

The observer pattern is a behavioral design pattern that defines a one-to-many
dependency between objects so that when one object changes state, all its
dependents are notified and updated automatically.

In this example, we have an `Inventory` class that represents an inventory
of products. The inventory can have multiple observers that are interested 
in the product and quantity changes. The `ConsoleObserver` class is an observe
that prints the product and quantity of the inventory whenever it changes.
"""

class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    # Native Python syntax that uses the @property decorator 
    # to define a getter method for the product attribute
    @property
    def product(self):
        return self._product
    
    # Native Python syntax that uses the @<attribute>.setter decorator
    # to define a setter method for the product attribute
    @product.setter 
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()
    
    # Helper method to called when the state changes
    def _update_observers(self):
        # Notify the observers
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory
    
    # The __call__ method is called when the instance is "called" as a function
    def __call__(self):
        if self.inventory.quantity > 4:
            print(f"{self.inventory.product} has {self.inventory.quantity}, overload warning!")
        print(self.inventory.product)
        print(self.inventory.quantity)


if __name__ == '__main__':
    # Create an inventory
    inventory = Inventory()
    # Create observers
    console_observer = ConsoleObserver(inventory)
    # Attach observers to the inventory
    inventory.attach(console_observer)
    # Update the inventory
    inventory.product = "Apples"
    # Should print: Apples -> 0 -> Apples -> 0
    inventory.quantity = 10 
    # Should print: Apples -> 10 -> Apples has 10, overload warning!