# Here's a simple Least Recently Used (LRU) cache implementation in Python using a list. In this example, 
# we'll use a list to store cache items in the order they were accessed. 
# When the cache is full, the least recently used item (at the end of the list) will be removed to make space for new items.

# For simplicity:

# The cache will have a fixed size.
# When an item is accessed, it moves to the front of the list.
# When a new item is added, the least recently used item will be removed if the cache is full.


# Explanation:

# put(item): Adds a new item to the cache.
# If the item is already in the cache, it removes it first to update its position.
# If the cache is full, it removes the least recently used item (last item in the list).
# It then inserts the new item at the beginning (most recently used position).

# get(item): Checks if an item is in the cache.
# If found, it moves the item to the front (making it the most recently used) and returns the item.
# If not found, returns -1.


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []  # List to store the cache items
        self.capacity = capacity  # Fixed size for the cache
    
    def get(self, item):
        # Check if the item is in the cache
        if item in self.cache:
            # Move the accessed item to the front (most recently used)
            self.cache.remove(item)
            self.cache.insert(0, item)
            return item  # Return the item if found
        return -1  # Return -1 if the item is not in cache

    def put(self, item):
        # If the item is already in cache, remove it (update position)
        if item in self.cache:
            self.cache.remove(item)
        # If the cache is at capacity, remove the least recently used item
        elif len(self.cache) >= self.capacity:
            self.cache.pop()  # Remove last item in the list (least recently used)
        # Insert the new item at the front (most recently used)
        self.cache.insert(0, item)
    
    def display(self):
        print("Current Cache State:", self.cache)

# Usage example
cache = LRUCache(3)  # Cache with capacity 3
cache.put(1)
cache.put(2)
cache.put(3)
cache.display()  # Output: [3, 2, 1]

cache.get(2)     # Access item 2, making it most recently used
cache.display()  # Output: [2, 3, 1]

cache.put(4)     # Add item 4, evict the least recently used item (1)
cache.display()  # Output: [4, 2, 3]

cache.get(1)     # Try to access item 1 (not in cache)
# Output: -1 because 1 was evicted
