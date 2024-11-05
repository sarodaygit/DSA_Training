''' 
       8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
'''

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

    # Recursive DFS Search using Preorder Traversal
    def dfs_search_recursive(self, value):
        print(f"Starting recursive DFS search for value: {value}")
        result = self._dfs_search_recursive(self.root, value)
        if result:
            print(f"Value {value} found in the tree.")
        else:
            print(f"Value {value} not found in the tree.")
        return result

    def _dfs_search_recursive(self, cur_node, value):
        if cur_node is None:
            return False  # Base case: reached a leaf or empty tree
        
        # Print the current node being checked
        print(f"Visiting node with value: {cur_node.data}")
        
        if cur_node.data == value:
            return True  # Value found at the current node
        
        # Search left and right children
        return self._dfs_search_recursive(cur_node.left, value) or self._dfs_search_recursive(cur_node.right, value)
    
    def dfs_search_iterative(self, value):
        print(f"Starting iterative DFS search for value: {value}")
        
        if not self.root:
            print("The tree is empty.")
            return False

        stack = [self.root]  # Start with the root node in the stack
        while stack:
            cur_node = stack.pop()  # Pop the last node in the stack
            print(f"Visiting node with value: {cur_node.data}")  # Print the current node being checked

            if cur_node.data == value:
                print(f"Value {value} found in the tree.")
                return True  # Value found

            # Add right and left children to the stack (right first, so left is processed first)
            if cur_node.right:
                stack.append(cur_node.right)
                print(f"Adding node with value {cur_node.right.data} to the stack (right child).")
            if cur_node.left:
                stack.append(cur_node.left)
                print(f"Adding node with value {cur_node.left.data} to the stack (left child).")
        
        print(f"Value {value} not found in the tree.")
        return False  # If the loop completes without finding the value

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

bst.dfs_search_recursive(7)  # Example search for 7
bst.dfs_search_recursive(2)  # Example search for 2 (not in tree)

bst.dfs_search_iterative(14)
bst.dfs_search_iterative(0)

