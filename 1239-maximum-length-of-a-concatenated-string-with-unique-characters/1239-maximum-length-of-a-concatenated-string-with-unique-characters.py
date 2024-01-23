class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.best = 0
        
        def recur(i, letters):
            letters = letters.copy()
            if i == len(arr):
                self.best = max(self.best, len(letters))
                return
            
            recur(i+1, letters)
            
            word = arr[i]
            if len(word) == len(set(word)):
                for c in word:
                    if c in letters:
                        return
                    letters.add(c)
                recur(i+1, letters)
        
        recur(0, set())
        return self.best