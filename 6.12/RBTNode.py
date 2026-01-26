from BSTNode import BSTNode

class RBTNode(BSTNode):
    red = 'red'
    black = 'black'

    # Initialize the RBTNode with the given key. Height is assigned with 0.
    # super() sets left, right, and parent to None.
    def __init__(self, node_key):
        super().__init__(node_key)
        self.color = self.red

    def __str__(self):
        return str(self.get_key()) + " R" if self.is_red() else " B"

    def get(self):
        return self.color

    # Return True if both child nodes are black. A child assigned with None is
    # considered to be black.
    def both_children_are_black(self):
        left = self.get_left()
        if left and left.is_red():
            return False
        right = self.get_right()
        if right and right.is_red():
            return False

        return True

    def get_grand_parent(self):
        return self.get_parent().get_parent() if self.get_parent() else None

    # Return this node's sibling, or None if this node does not have a sibling
    def get_sibling(self):
        parent = self.get_parent()
        if parent:
            if self == parent.get_left():
                return parent.get_right()
            else:
                return parent.get_left()
        return None

    # Return the uncle of this node
    def get_uncle(self):
        grandparent = self.get_grand_parent()
        if not grandparent:
            return None
        elif grandparent.get_left() == self.get_parent():
                return grandparent.get_right()
        else:
            return grandparent.get_left()

    # Return True if this node is red, False otherwise
    def is_red(self):
        return self.color == self.red

    # Return True if this node is black, False otherwise
    def is_black(self):
        return self.color == self.black

    def is_parent_null(self):
        return not self.get_parent()

    # Return True if this node's right child is non-null and red. Returns
    # False otherwise.
    def is_left_child_red(self):
        return self.get_left() and self.get_left().get() == self.red

    # Return True if this node's right child is non-null and red. Returns
    # False otherwise.
    def is_right_child_red(self):
        return self.get_right() and self.get_right().get() == self.red
