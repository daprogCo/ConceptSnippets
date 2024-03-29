"""
### Example of the strategy pattern in Python ###

The strategy pattern is a behavioral design pattern that enables selecting
an algorithm at runtime. It defines a family of algorithms, encapsulates each
algorithm, and makes the algorithms interchangeable within that family.

Interfaces or abstract classes are used to define the strategy, and concrete
classes implement the strategy. The client can choose the appropriate strategy
and use it without knowing the implementation details.

In this example, we have a `Sorter` class that uses a `SortStrategy` interface
to sort a collection of elements. The `SortStrategy` interface defines a `sort`
method that must be implemented by concrete strategies such as
`QuickSortStrategy` and `MergeSortStrategy`. The `Sorter` class can use any
of these strategies to sort the collection of elements.

The strategy pattern is useful when you want to switch between different
algorithms at runtime or when you want to isolate the algorithm implementation
from the client code.
"""
# abc is a module that provides the infrastructure for defining Abstract Base
# Classes in Python more details can be found at https://docs.python.org/3/library/abc.html (PEP 3119)

from abc import ABC, abstractmethod

# Abstract class or interface that defines the strategy
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, collection):
        pass

# Child classes of SortStrategy that are concrete strategies
class QuickSortStrategy(SortStrategy):
    def sort(self, collection):
        # Implement Quick Sort algorithm
        # This is just a placeholder, the actual implementation is not provided
        # here and I used the built-in sorted function for simplicity
        print("Using Quick Sort algorithm")
        return sorted(collection)

class MergeSortStrategy(SortStrategy):
    def sort(self, collection):
        # Implement Merge Sort algorithm
        # This is just a placeholder, the actual implementation is not provided
        # here and I used the built-in sorted function for simplicity
        print("Using Merge Sort algorithm")
        return sorted(collection)

# Context class or the client class that uses the strategy at runtime 
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_collection(self, collection):
        return self.strategy.sort(collection)

if __name__ == "__main__":
    collection = [3, 1, 4, 1, 5, 9, 2, 6]
    quick_sorter = Sorter(QuickSortStrategy())
    sorted_collection = quick_sorter.sort_collection(collection)
    print(sorted_collection)

    # Dynamically change the strategy at runtime
    quick_sorter.set_strategy(MergeSortStrategy())
    sorted_collection = quick_sorter.sort_collection(collection)
    print("Changed to mergeSort:", sorted_collection)

