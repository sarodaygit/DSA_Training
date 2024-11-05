class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
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
        else:
            print("Value already in tree!")

    def is_bst_satisfied(self):
        # Call the helper function with the root node and default bounds
        return self.helper(self.root, float('-inf'), float('inf'))

    # Helper function to validate BST properties using a range for each node
    def helper(self, node, lower, upper):
        if not node:  # An empty node satisfies BST properties
            return True

        val = node.data
        # Check if the node's value violates the BST properties
        if val <= lower or val >= upper:
            return False

        # Recursively check the right subtree with updated lower bound
        if not self.helper(node.right, val, upper):
            return False
        # Recursively check the left subtree with updated upper bound
        if not self.helper(node.left, lower, val):
            return False
        return True

# Example usage
bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print("BST is valid:", bst.is_bst_satisfied())  # Expected: True

# Creating an invalid tree for testing
tree = BST()
tree.root = Node(1)
tree.root.left = Node(-4)
tree.root.right = Node(3)
tree.root.left.left = Node(-5)
tree.root.left.right = Node(0)
tree.root.right.left = Node(2)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(-8)  # Invalid position for -8

print("Manual Tree Structure Check (should be invalid):")
print("Tree is valid BST:", tree.is_bst_satisfied())  # Expected: False
