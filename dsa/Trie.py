class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                print(curr.children)
            curr = curr.children[c]
        curr.isLast = True
        print(curr.children)
    
    def search(self, word) -> bool:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isLast
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
    
def main():
    t = Trie()
    t.insert('a')
    t.insert('b')
    t.insert('c')
    t.insert('d')
    t.insert('e')
    
    
    
    
    
if __name__ == '__main__':
    main()
        
        