import unittest
from BST import BST

class TestBST(unittest.TestCase):
    def test_empty_tree(self):
        bst = BST()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.size(), 0)
        self.assertIsNone(bst.find(10))
        self.assertEqual(bst.height(bst.root), -1)

    def test_add_and_find(self):
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.size(), len(values))
        for v in values:
            node = bst.find(v)
            self.assertIsNotNone(node)
            self.assertEqual(node.value, v)
        self.assertIsNone(bst.find(999))

    def test_duplicates_not_added(self):
        bst = BST()
        bst.add(5)
        bst.add(5)  # duplicate
        self.assertEqual(bst.size(), 1)
        self.assertIsNotNone(bst.find(5))

    def test_height(self):
        bst = BST()
        for v in [5, 3, 7, 2, 4, 6, 8]:
            bst.add(v)
        # Balanced-ish tree -> height should be 2 (root level 0)
        self.assertEqual(bst.height(bst.root), 2)

    def test_remove_leaf(self):
        bst = BST()
        for v in [5, 3, 7, 2]:
            bst.add(v)
        initial_size = bst.size()
        bst.remove(2)  # remove leaf
        self.assertIsNone(bst.find(2))
        self.assertEqual(bst.size(), initial_size - 1)
        # other nodes remain
        self.assertIsNotNone(bst.find(3))
        self.assertIsNotNone(bst.find(5))

    def test_remove_node_with_one_child(self):
        bst = BST()
        for v in [5, 3, 2]:  # 3 has only left child 2
            bst.add(v)
        bst.remove(3)
        self.assertIsNone(bst.find(3))
        # 2 should still be present and now be left child of 5
        node2 = bst.find(2)
        self.assertIsNotNone(node2)
        self.assertEqual(bst.root.left.value, 2)
        self.assertEqual(bst.size(), 2)

    def test_remove_node_with_two_children(self):
        bst = BST()
        for v in [5, 3, 7, 2, 4, 6, 8]:
            bst.add(v)
        initial_size = bst.size()
        bst.remove(3)  # 3 has two children 2 and 4; successor 4 should replace it
        self.assertIsNone(bst.find(3))
        # root.left should now have value 4 (successor)
        self.assertEqual(bst.root.left.value, 4)
        self.assertIsNotNone(bst.find(2))
        self.assertEqual(bst.size(), initial_size - 1)

    def test_remove_root_variants(self):
        # remove sole root
        bst = BST()
        bst.add(10)
        bst.remove(10)
        self.assertTrue(bst.is_empty())
        self.assertIsNone(bst.root)
        self.assertEqual(bst.size(), 0)

        # remove root with one child
        bst = BST()
        bst.add(10)
        bst.add(5)
        bst.remove(10)
        self.assertEqual(bst.root.value, 5)
        self.assertEqual(bst.size(), 1)

        # remove root with two children
        bst = BST()
        for v in [10, 5, 15, 3, 7]:
            bst.add(v)
        bst.remove(10)
        # new root should be successor (likely 15 or 5 replaced by successor logic)
        self.assertEqual(bst.size(), 4)
        self.assertIsNone(bst.find(10))

    def test_remove_nonexistent_key_no_change(self):
        bst = BST()
        for v in [1, 2, 3]:
            bst.add(v)
        size_before = bst.size()
        bst.remove(999)  # not present
        self.assertEqual(bst.size(), size_before)
    
    def test_inorder_traversal_empty_tree(self):
        """Test inorder traversal on empty tree"""
        bst = BST()
        result = bst.inorder_traversal(bst.root)
        self.assertEqual(result, [])

    def test_inorder_traversal_single_node(self):
        """Test inorder traversal with single node"""
        bst = BST()
        bst.add(5)
        result = bst.inorder_traversal(bst.root)
        self.assertEqual(result, [5])

    def test_inorder_traversal_multiple_nodes(self):
        """Test inorder traversal returns values in sorted order"""
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        result = bst.inorder_traversal(bst.root)
        expected = sorted(values)
        self.assertEqual(result, expected)

    def test_preorder_traversal_empty_tree(self):
        """Test preorder traversal on empty tree"""
        bst = BST()
        result = bst.preorder_traversal(bst.root)
        self.assertEqual(result, [])

    def test_preorder_traversal_single_node(self):
        """Test preorder traversal with single node"""
        bst = BST()
        bst.add(5)
        result = bst.preorder_traversal(bst.root)
        self.assertEqual(result, [5])

    def test_preorder_traversal_multiple_nodes(self):
        """Test preorder traversal visits root first"""
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        result = bst.preorder_traversal(bst.root)
        # Root should be first
        self.assertEqual(result[0], 5)
        # All values should be present
        self.assertEqual(sorted(result), sorted(values))

    def test_postorder_traversal_empty_tree(self):
        """Test postorder traversal on empty tree"""
        bst = BST()
        result = bst.postorder_traversal(bst.root)
        self.assertEqual(result, [])

    def test_postorder_traversal_single_node(self):
        """Test postorder traversal with single node"""
        bst = BST()
        bst.add(5)
        result = bst.postorder_traversal(bst.root)
        self.assertEqual(result, [5])

    def test_postorder_traversal_multiple_nodes(self):
        """Test postorder traversal visits root last"""
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        result = bst.postorder_traversal(bst.root)
        # Root should be last
        self.assertEqual(result[-1], 5)
        # All values should be present
        self.assertEqual(sorted(result), sorted(values))

    def test_inorder_traversal_after_removal(self):
        """Test inorder traversal after removing nodes"""
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        
        bst.remove(3)
        result = bst.inorder_traversal(bst.root)
        expected = sorted([v for v in values if v != 3])
        self.assertEqual(result, expected)

    def test_all_traversals_contain_same_elements(self):
        """Test that all traversals contain the same elements"""
        bst = BST()
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            bst.add(v)
        
        inorder = bst.inorder_traversal(bst.root)
        preorder = bst.preorder_traversal(bst.root)
        postorder = bst.postorder_traversal(bst.root)
        
        self.assertEqual(sorted(inorder), sorted(values))
        self.assertEqual(sorted(preorder), sorted(values))
        self.assertEqual(sorted(postorder), sorted(values))


if __name__ == "__main__":
    unittest.main(verbosity=2)