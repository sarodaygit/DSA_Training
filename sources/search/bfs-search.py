'''        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
'''

from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

    # BFS Search for a given value
    def bfs_search(self, value):
        print(f"Starting BFS search for value: {value}")
        
        if not self.root:
            print("The tree is empty.")
            return False
        
        # Initialize queue with root node
        queue = deque([self.root])
        
        while queue:
            cur_node = queue.popleft()  # Dequeue the front node
            print(f"Visiting node with value: {cur_node.data}")  # Print the current node

            if cur_node.data == value:
                print(f"Value {value} found in the tree.")
                return True
            
            # Enqueue the left and right children of the current node
            if cur_node.left:
                queue.append(cur_node.left)
                print(f"Adding node with value {cur_node.left.data} to the queue (left child).")
            if cur_node.right:
                queue.append(cur_node.right)
                print(f"Adding node with value {cur_node.right.data} to the queue (right child).")
        
        print(f"Value {value} not found in the tree.")
        return False  # Value not found after full traversal

# Example Usage
bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

bst.bfs_search(7)  # Example search for 7
bst.bfs_search(2)  # Example search for 2 (not in tree)
