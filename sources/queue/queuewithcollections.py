from collections import deque

class Queue:
    def __init__(self):
        # Initialize an empty deque for the queue
        self.queue = deque()

    def enqueue(self, item):
        # Add an item to the rear of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None  # Return None if the queue is empty

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return None  # Return None if the queue is empty

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front item:", q.peek())  # Output: Front item: 1
    print("Queue size:", q.size())   # Output: Queue size: 3

    print("Dequeue:", q.dequeue())    # Output: Dequeue: 1
    print("Queue size after dequeue:", q.size())  # Output: Queue size after dequeue: 2
