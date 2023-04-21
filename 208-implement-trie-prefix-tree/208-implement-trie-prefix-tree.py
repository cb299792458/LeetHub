class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        
        for char in word:
            i = ord(char)-ord('a')
            if not current.children[i]: current.children[i] = Node()
            current = current.children[i]
        
        current.word = True

    def search(self, word: str) -> bool:
        current = self.root
        
        for char in word:
            i = ord(char)-ord('a')
            if not current.children[i]: return False
            current = current.children[i]

        return current.word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for char in prefix:
            i = ord(char)-ord('a')
            if not current.children[i]: return False
            current = current.children[i]

        return current != None
        

class Node:
    def __init__(self):
        self.word = False
        self.children = [None]*26