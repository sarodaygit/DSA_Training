from collections import deque

class StackWithDeque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack elements:", list(self.items))


# Example usage
stack_deque = StackWithDeque()
stack_deque.push(1)
stack_deque.push(2)
stack_deque.push(3)
print(stack_deque.pop())  # Output: 3
