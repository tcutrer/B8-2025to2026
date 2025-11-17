"""
Tatum Cutrer
B8 Algorithms and Data Structures
File Name: BST.py
Date: 11/11/2025

This module implements a Binary Search Tree (BST) with insertion, search, and removal functionalities.
"""

import pair

class BST:
    class Node:
        def __init__(self, key, count=1):
            self.left = None
            self.right = None
            self.value = pair.Pair(key, count)
    
    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        """Return the number of nodes in the BST."""
        return self._size
    
    def is_empty(self):
        """Check if the BST is empty."""
        return self._size == 0
    
    def find(self, key):
        """Find a node with the given key in the BST."""
        currentNode = self.root
        while currentNode is not None:
            if key == currentNode.value.letter:
                return currentNode
            elif key < currentNode.value.letter:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None

    
    def add(self, key, count=1):
        """Insert a new key into the BST."""
        currentNode = self.root
        newNode = self.Node(key, count)
        if self.is_empty():
            self.root = newNode
            self._size += 1
            return
        while True:
            if key < currentNode.value.letter:
                if currentNode.left is None:
                    currentNode.left = newNode
                    self._size += 1
                    return
                currentNode = currentNode.left
            elif key > currentNode.value.letter:
                if currentNode.right is None:
                    currentNode.right = newNode
                    self._size += 1
                    return
                currentNode = currentNode.right
            else:
                # Key already exists, do not insert duplicates
                return
            
    def height(self, node):
        """Calculate the height of the BST."""
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
    
    def remove(self, key):
        """Remove a node with the given key from the BST."""
        if self.is_empty():
            return
        currentNode = self.root
        parentNode = None
        while currentNode is not None and currentNode.value.letter != key:
            parentNode = currentNode
            if key < currentNode.value.letter:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if currentNode is None:
            return  # Key not found
        # Node with only one child or no child
        if currentNode.left is None or currentNode.right is None:
            if currentNode.left is not None:
                child = currentNode.left
            else:
                child = currentNode.right
            if parentNode is None:
                self.root = child
            elif parentNode.left == currentNode:
                parentNode.left = child
            else:
                parentNode.right = child
        else:
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successorParent = currentNode
            successor = currentNode.right
            while successor.left is not None:
                successorParent = successor
                successor = successor.left
            currentNode.value.letter = successor.value.letter
            if successorParent.left == successor:
                successorParent.left = successor.right
            else:
                successorParent.right = successor.right
        self._size -= 1

    def inorder_traversal(self, node, result=None):
        """Inorder traversal: left, root, right (returns sorted list)"""
        if result is None:
            result = []
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node.value.letter)
            self.inorder_traversal(node.right, result)
        return result
    
    def preorder_traversal(self, node, result=None):
        """Preorder traversal: root, left, right"""
        if result is None:
            result = []
        if node is not None:
            result.append(node.value.letter)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result
    
    def postorder_traversal(self, node, result=None):
        """Postorder traversal: left, right, root"""
        if result is None:
            result = []
        if node is not None:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value.letter)
        return result
