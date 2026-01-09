class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isLeaf
    
    def is_prefix(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True
