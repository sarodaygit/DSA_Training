class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []

    def is_empty(self):
        # Return True if the queue is empty, otherwise False
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        # If the queue is empty, raise an error
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        # Return the front item of the queue without removing it
        # If the queue is empty, raise an error
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

    def __str__(self):
        # Return a string representation of the queue for easy viewing
        return "Queue: " + str(self.items)


# Example usage
q = Queue()               # Create a new queue
q.enqueue(1)              # Add 1 to the queue
q.enqueue(2)              # Add 2 to the queue
q.enqueue(3)              # Add 3 to the queue
print(q)                  # Output the queue: Queue: [1, 2, 3]
print(q.dequeue())        # Remove and output the front item: 1
print(q)                  # Output the queue after dequeue: Queue: [2, 3]
print(q.peek())           # Output the current front item: 2
print(q.size())           # Output the size of the queue: 2
