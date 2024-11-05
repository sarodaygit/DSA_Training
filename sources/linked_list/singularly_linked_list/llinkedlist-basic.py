class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Initially, the next reference is None

class ll:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(100)
        new_node.next = self.head
        self.head = new_node
        

# Creating nodes
node1 = Node(1)
node2 = Node(2)

# Linking nodes
node1.next = node2

# Checking memory addresses
print(id(node1), id(node2))  # Unique memory addresses for each node
print(node1.next.__dict__, node2.__dict__)