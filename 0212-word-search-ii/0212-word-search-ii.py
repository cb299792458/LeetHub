class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False
    
    def insert(self, word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.word = word
        
        
    def remove(self, word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.word = False
        
        curr = self
        for char in word:
            if not curr.children[char].children and not curr.children[char].word:
                del curr.children[char]
                return
            else:
                curr = curr.children[char]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        self.words = []
        
        R,C = len(board), len(board[0])
        
        def backtrack(r,c,t,path):
            if r<0 or c<0 or r==R or c==C:
                return
            
            if (r,c) in path:
                return
            path.add((r,c))
            
            char = board[r][c]
            if char not in t.children:
                return
            
            new_t = t.children[char]
            if new_t.word:
                self.words.append(new_t.word)
                trie.remove(new_t.word)
                
            backtrack(r+1,c,new_t,path.copy())
            backtrack(r-1,c,new_t,path.copy())
            backtrack(r,c+1,new_t,path.copy())
            backtrack(r,c-1,new_t,path.copy())
            
        for r in range(R):
            for c in range(C):
                backtrack(r,c,trie,set())
        return self.words