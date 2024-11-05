class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the item from the top of the stack
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        # Return the top item without removing it from the stack
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def display(self):
        # Print the stack elements
        print("Stack elements:", self.items)


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Top element:", stack.peek())  # Output: Top element: 3
    print("Stack size:", stack.size())    # Output: Stack size: 3

    stack.display()                        # Output: Stack elements: [1, 2, 3]

    print("Popped element:", stack.pop())  # Output: Popped element: 3
    print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

    stack.display()                        # Output: Stack elements: [1, 2]
