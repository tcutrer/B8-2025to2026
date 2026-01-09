from AVLTree import AVLTree
from ExtendedAVLNode import ExtendedAVLNode

class ExtendedAVLTree(AVLTree):
    def __init__(self):
        super().__init__()

    # Each node in an ExtendedAVLTree is an ExtendedAVLNode
    def make_new_node(self, key):
        return ExtendedAVLNode(key)

    # TODO: Type your code here

    def get_nth_key(self, n):
        # TODO: Type your code here
        return 0