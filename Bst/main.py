from BST import *

def load_tree(filename):
    """Load a BST from a file containing words."""
    bst = BST()
    text = ""
    with open(filename, 'r') as file:
        text = file.read().lower()
    for char in text:
        if char.isspace():  # Consider only alphabetic characters
            continue
        if bst.find(char) is None:
            bst.add(char)
        else:
            node = bst.find(char)
            node.value.count += 1
    return bst

def main():
    bst = load_tree('Bst/around-the-world-in-80-days-3.txt')
    print("Inorder Traversal (letters in sorted order):")
    print(bst.inorder_traversal(bst.root))
    print("\nLetter Frequencies:")
    def print_frequencies(node):
        if node is not None:
            print_frequencies(node.left)
            print(f"{node.value.letter}: {node.value.count}")
            print_frequencies(node.right)
    print_frequencies(bst.root)

if __name__ == "__main__":
    main()