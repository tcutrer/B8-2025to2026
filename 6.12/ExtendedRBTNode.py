from RBTNode import RBTNode

class ExtendedRBTNode(RBTNode):

    def __init__(self, node_key):
        super().__init__(node_key)
        self.subtree_key_count = 1

    def get_subtree_key_count(self):
        return self.subtree_key_count

    def update_subtree_key_count(self):
        left_count = self.left.get_subtree_key_count() if self.left else 0
        right_count = self.right.get_subtree_key_count() if self.right else 0
        self.subtree_key_count = 1 + left_count + right_count