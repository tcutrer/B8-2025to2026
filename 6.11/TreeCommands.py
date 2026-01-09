from abc import ABC, abstractmethod
from BinarySearchTree import BinarySearchTree
from BSTNodeListVisitor import BSTNodeListVisitor

class TreeTestCommand:
    @abstractmethod
    def execute(self):
        pass

class TreeInsertCommand(TreeTestCommand):
    def __init__(self, keys):
        self.keys_to_insert = keys

    def execute(self, tree, test_feedback):
        # If no keys to insert, return True immediately
        if 0 == len(self.keys_to_insert):
            return True

        # Begin feedback message
        test_feedback.write(f"Inserting keys: {self.keys_to_insert}")

        for key in self.keys_to_insert:
            tree.insert_key(key)

        return True

class TreeRemoveCommand(TreeTestCommand):
    def __init__(self, keys):
        self.keys_to_remove = keys

    def execute(self, tree, test_feedback):
        if len(self.keys_to_remove) > 0:
            # Begin feedback message
            test_feedback.write(f"Removing keys: {self.keys_to_remove}")
            # Remove keys
            for key in self.keys_to_remove:
                tree.remove_key(key)
        return True

class TreeVerifyKeysCommand(TreeTestCommand):
    def __init__(self, keys):
        self.expected_keys = keys

    def execute(self, tree, test_feedback):
        # Create a BSTNodeStringVisitor and do an in order traversal.
        visitor = BSTNodeListVisitor()
        tree.in_order(visitor)

        # The visitor determines if a circular reference exists.
        if visitor.has_circular_reference():
            test_feedback.write(f"FAIL: Tree traversal encountered the same " +
                "node more than once, so a circulare reference exists")
            return False

        # Make a list of keys from the visitor's string of nodes
        actual = []
        for node in visitor.visited_nodes:
            actual.append(node.get_key())

        # Compare actual to expected
        passed = True

        if len(actual) == len(self.expected_keys):
            for actual_key, expected_key in zip(actual, self.expected_keys):
                if actual_key != expected_key:
                    passed = False
        else:
            passed = False

        # Display feedback and return
        test_feedback.write(
            f"{'PASS' if passed else 'FAIL'}: Inorder key verification\n" +
            f"  Expected: {self.expected_keys}\n" +
            f"  Actual:   {actual}")
        return passed

class TreeGetNthCommand(TreeTestCommand):
    def __init__(self, n, expected_key):
        self.n = n
        self.expected_key = expected_key

    def execute(self, tree, test_feedback):
        actual_key = tree.get_nth_key(self.n)
        if actual_key == self.expected_key:
            test_feedback.write(f"PASS: get_nth_key({self.n}) returned " +
                f"{actual_key}")
            return True

        # Actual key does not equal expected
        test_feedback.write(f"FAIL: get_nth_key({self.n}) returned " +
            f"{actual_key}, but expected key is {self.expected_key}")
        return False

class TreeVerifySubtreeCountsCommand(TreeTestCommand):
    def __init__(self, expected_key_count_pairs):
        self.expected_pairs = expected_key_count_pairs

    def execute(self, tree, test_feedback):
        # Create a BSTNodeStringVisitor and do an in order traversal
        visitor = BSTNodeListVisitor()
        tree.in_order(visitor)

        # Compare actual to expected
        passed = True
        if len(visitor.visited_nodes) == len(self.expected_pairs):
            for actual_node, expected_pair in zip(visitor.visited_nodes, self.expected_pairs):
                # Get the actual node's subtree key count
                actual_count = actual_node.get_subtree_key_count()

                # Compare actual vs. expected subtree key count
                if actual_count != expected_pair[1]: 
                    test_feedback.write("FAIL: Node with key " +
                        f"{actual_node.get_key()} has a subtree key count " +
                        f"of {actual_count}, but the expected subtree key " +
                        f"count is {expected_pair[1]}")
                    passed = False
                else:
                    test_feedback.write("PASS: Node with key " +
                        f"{actual_node.get_key()} has a subtree key count " +
                        f"of {actual_count}")

            if not passed:
                return  False

            # Display results
            test_feedback.write(f"PASS: All {len(self.expected_pairs)} " +
                "nodes have correct subtree key counts")
            return True

        # Give feedback indicating that the tree's number of nodes is incorrect
        phrase = ("only one node was"
                  if len(self.expected_pairs) == 1
                  else f"{len(self.expected_pairs)} nodes were")
        test_feedback.write("FAIL: Traversal through tree encountered " +
            f"{len(visitor.visited_nodes)} nodes before either stopping or " +
            f"encountering a circular reference. However, {phrase} expected " +
            "in the tree.")
        return False
