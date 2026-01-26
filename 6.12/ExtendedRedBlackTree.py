from RedBlackTree import RedBlackTree
from ExtendedRBTNode import ExtendedRBTNode

class ExtendedRedBlackTree(RedBlackTree):
    def __init__(self):
        super().__init__()

    # Each node in an ExtendedRedBlackTree is an ExtendedRBTNode
    def make_new_node(self, key):
        return ExtendedRBTNode(key)

    def insert_node(self, node):
        super().insert_node(node)

        node = node
        while node:
            node.update_subtree_key_count()
            node = node.get_parent()

    def remove_node(self, node_to_remove):
        parent_of_removed = node_to_remove.get_parent()
        super().remove_node(node_to_remove)

        node = parent_of_removed
        while node:
            node.update_subtree_key_count()
            node = node.get_parent()

        return True

    def rotate_left(self, node):
        # Perform the rotation
        new_root = super().rotate_left(node)
        
        # Update subtree key counts bottom-up from the rotated nodes
        node.update_subtree_key_count()
        new_root.update_subtree_key_count()
        
        return new_root

    def rotate_right(self, node):
        # Perform the rotation
        new_root = super().rotate_right(node)
        
        # Update subtree key counts bottom-up from the rotated nodes
        node.update_subtree_key_count()
        new_root.update_subtree_key_count()
        
        return new_root

    def get_nth_key(self, n):
        if not self.root or n < 0:
            return None
        return self._get_nth_helper(self.root, n)

    def _get_nth_helper(self, node, n):
        left_count = node.left.get_subtree_key_count() if node.left else 0
        if n == left_count:
            return node.get_key()
        elif n < left_count:
            return self._get_nth_helper(node.left, n)
        else:
            return self._get_nth_helper(node.right, n - left_count - 1)