from BinarySearchTree import BinarySearchTree
from RBTNode import RBTNode

class RedBlackTree(BinarySearchTree):
    def __init__(self):
        # Note: Parent class's constructor does all needed work
        super().__init__()

    def prepare_for_removal(self, node):
        if self.try_case1(node):
            return

        sibling = node.get_sibling()
        if self.try_case2(node, sibling):
            sibling = node.get_sibling()

        if self.try_case3(node, sibling):
            return

        if self.try_case4(node, sibling):
            return

        if self.try_case5(node, sibling):
            sibling = node.get_sibling()

        if self.try_case6(node, sibling):
            sibling = node.get_sibling()

        node_parent = node.get_parent()
        sibling.color = node_parent.color
        node_parent.color = RBTNode.black
        if node == node_parent.get_left():
            sibling.get_right().color = RBTNode.black
            self.rotate_left(node_parent)
        else:
            sibling.get_left().color = RBTNode.black
            self.rotate_right(node_parent)

    def try_case1(self, node):
        if node.is_red() or node.is_parent_null():
            return True
        else:
            return False # not case 1

    def try_case2(self, node, sibling):
        if sibling.is_red():
            node_parent = node.get_parent()
            node_parent.color = RBTNode.red
            sibling.color = RBTNode.black
            if node == node_parent.get_left():
                self.rotate_left(node_parent)
            else:
                self.rotate_right(node_parent)
            return True
        else:
            return False # not case 2

    def try_case3(self, node, sibling):
        node_parent = node.get_parent()
        if node_parent.is_black() and sibling.both_children_are_black():
            sibling.color = RBTNode.red
            self.prepare_for_removal(node_parent)
            return True
        else:
            return False # not case 3

    def try_case4(self, node, sibling):
        node_parent = node.get_parent()
        if node_parent.is_red() and sibling.both_children_are_black():
            node_parent.color = RBTNode.black
            sibling.color = RBTNode.red
            return True
        else:
            return False # not case 4

    def try_case5(self, node, sibling):
        if (sibling.is_left_child_red() and
            not sibling.is_right_child_red() and
            node == node.get_parent().get_left()
            ):
            sibling.color = RBTNode.red
            sibling.get_left().color = RBTNode.black
            self.rotate_right(sibling)
            return True
        else:
            return False # not case 5

    def try_case6(self, node, sibling):
        if (not sibling.is_left_child_red() and
            sibling.is_right_child_red() and
            node == node.get_parent().get_right()
            ):
            sibling.color = RBTNode.red
            sibling.get_right().color = RBTNode.black
            self.rotate_left(sibling)
            return True
        else:
            return False # not case 6

    def insert_node(self, node):
        # Red-black tree insertion starts with the standard BST insertion
        super().insert_node(node)

        # Color the node red, then balance
        node.color = RBTNode.red
        self.insertion_balance(node)

    def make_new_node(self, key):
        return RBTNode(key)

    def remove_node(self, bst_node):
        if not bst_node:
            return False

        node = bst_node
        if node.get_left() and node.get_right():
            # Get the node's predecessor
            predecessor_node = node.get_left()
            while predecessor_node.get_right():
                predecessor_node = predecessor_node.get_right()

            # Get predecessor's key, then recursively remove the predecessor node
            predecessor_key = predecessor_node.get_key()
            self.remove_node(predecessor_node)

            # Assign the node's key with the now-removed predecessor node's key
            node.set_key(predecessor_key)

            return True

        if node.is_black():
            self.prepare_for_removal(node)
        super().remove_node(node)

        # One special case if the root was changed to red
        root_node = self.get_root()
        if root_node and root_node.is_red():
            root_node.color = RBTNode.black

        return True

    def insertion_balance(self, node):
        parent = node.get_parent()

        # If node is the tree's root, then color node black and return
        if not parent:
            node.color = RBTNode.black
            return

        # If parent is black, then return without any changes
        if parent.is_black():
            return

        # Node's grandparent and uncle are needed for remaining operations
        grandparent = node.get_grand_parent()
        uncle = node.get_uncle()

        # If parent and uncle are both red, then color parent and uncle black,
        # color grandparent red, recursively balance gra
        if uncle and uncle.is_red():
            parent.color = uncle.color = RBTNode.black
            grandparent.color = RBTNode.red
            self.insertion_balance(grandparent)
            return

        # If node is parent's right child and parent is grandparent's left
        # child, then rotate left at parent, update node and parent to point to
        # parent and grandparent, respectively
        if node == parent.get_right() and parent == grandparent.get_left():
            self.rotate_left(parent)
            node = parent
            parent = node.get_parent()

        # Else if node is parent's left child and parent is grandparent's right
        # child, then rotate right at parent, update node and parent to point to
        # parent and grandparent, respectively
        elif node == parent.get_left() and parent == grandparent.get_right():
            self.rotate_right(parent)
            node = parent
            parent = node.get_parent()

        # Color parent black and grandparent red
        parent.color = RBTNode.black
        grandparent.color = RBTNode.red

        # If node is parent's left child, then rotate right at grandparent,
        # otherwise rotate left at grandparent
        if node == parent.get_left():
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def is_null_or_black(self, node):
        return node == None or node.is_black()

    def is_not_null_and_red(self, node):
        return node == None or node.is_red()
