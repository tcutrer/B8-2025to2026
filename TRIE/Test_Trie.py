from trie import Trie

def main():
    trie = Trie()
    arr = ["and", "ant", "do", "dad"]
    for s in arr:
        trie.insert(s)
    searchKeys = ["do", "gee", "bat"]
    for s in searchKeys:
        if trie.search(s):
            print("true", end= " ")
        else:
            print("false", end=" ")
    
    print()
    prefixKeys = ["ge", "ba", "do", "de"]
    for s in prefixKeys:
        if trie.is_prefix(s):
            print("true", end = " ")
        else:
            print("false", end = " ")

if __name__ == "__main__":
    main()