"""
### Example of the state pattern in Python ###

The state pattern is a behavioral design pattern that allows an object to change
its behavior when its internal state changes. It defines a family of algorithms,
encapsulates each algorithm, and makes the algorithms interchangeable 
within that family.

It's pretty similar to the strategy pattern, but the difference is that the
strategy pattern is used to switch between different algorithms, while the state
pattern is used to switch between different states of a single algorithm.

To implement the State Pattern, we require a context manager that furnishes
an interface for state transitions. Internally, this manager maintains
a reference to the current state.

It is useful when an object's behavior depends on its state and must change
dynamically depending on that state.
"""
# abc is a module that provides the infrastructure for defining Abstract Base
# Classes in Python more details can be found 
# at https://docs.python.org/3/library/abc.html (PEP 3119)

from abc import ABC, abstractmethod

# Abstract state that handles the behavior and transitions
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Child classes of State that are concrete states with different behaviors
# that can be encapsulated in the context manager
class LowercaseState(State):
    def handle(self):
        return "lowercase"

class UppercaseState(State):
    def handle(self):
        return "UPPERCASE"

class TitleCaseState(State):
    def handle(self):
        return "Title Case"

# Context manager or the client class that uses the state at runtime
class TextEditor:
    def __init__(self):
        # Initial state
        # This statement is where reside the difference from the strategy pattern
        self.state = LowercaseState()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state.handle()

# Encapsulated version of the TextEditor class  
class TextEditorEncapsulated:
    def __init__(self):
        self.lowercase_state = LowercaseState()
        self.uppercase_state = UppercaseState()
        self.titlecase_state = TitleCaseState()
        self.state = LowercaseState()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state.handle()
    
    def set_lowercase_state(self):
        self.state = self.lowercase_state

    def set_uppercase_state(self):
        self.state = self.uppercase_state

    def set_titlecase_state(self):
        self.state = self.titlecase_state
    


if __name__ == "__main__":
    # Example usage
    editor = TextEditor()
    print(editor.get_state())
    # Change the state
    editor.set_state(UppercaseState())
    print(editor.get_state())
    # Change the state again
    editor.set_state(TitleCaseState())
    print(editor.get_state())

    # Example usage of the encapsulated version
    editor = TextEditorEncapsulated()
    print(editor.get_state())
    # Change the state
    editor.set_uppercase_state()
    print(editor.get_state())
    # Change the state again
    editor.set_titlecase_state()
    print(editor.get_state())