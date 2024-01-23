class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.best = 0
        
        def recur(words, letters):
            letters = letters.copy()
            if not words:
                self.best = max(self.best, len(letters))
                return
            
            # skip
            recur(words[1:], letters)
            
            # take
            word = words[0]
            if len(word) == len(set(word)):
                for c in word:
                    if c in letters:
                        return
                    letters.add(c)
                recur(words[1:], letters)
        
        recur(arr, set())
        return self.best