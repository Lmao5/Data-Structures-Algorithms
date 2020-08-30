# The storage class for creating binary tree nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Implementation of the Binary Search Tree
class BinarySearchTree:
    # Creates an initially empty BST
    def __init__(self):
        self._root = None
        self._size = 0
    # Returns the total number of elements in the BST
    def __len__(self):
        return self._size


    # Insert new_node into the BST
    def insertNode(self, new_node):
        if self._root is None:
            self._root = new_node
            self._size += 1
        else:
            self._recInsertNode(self._root , new_node)

    # Helper method to insert new_node into the BST recursively
    # from start_node
    def _recInsertNode(self, start_node, new_node):
        if start_node.data < new_node.data:
            if start_node.right is None:
                start_node.right = new_node
                return
            else:
                self._recInsertNode(start_node.right ,new_node )
        else:
            if start_node.left is None:
                start_node.left = new_node
                return
            else:
                self._recInsertNode(start_node.left ,new_node )
