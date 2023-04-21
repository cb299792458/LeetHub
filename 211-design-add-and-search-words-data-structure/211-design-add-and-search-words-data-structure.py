class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        
        for char in word:
            if current.children.get(char)==None: current.children[char] = Node()
            current = current.children[char]
            
        current.end_of_word = True

    def search(self, word: str) -> bool:
        return self.root.search(word)

class Node:
    def __init__(self):
        self.end_of_word = False
        self.children = dict()
        
    def search(self,word):
        # base case
        if word=='': return self.end_of_word
        
        # recursive case
        if word[0]!='.':
            if self.children.get(word[0])==None: return False
            return self.children[word[0]].search(word[1:])
        else:
            # res = False
            for key in self.children.keys():
                if self.children[key].search(word[1:]):
                    return True
            return False