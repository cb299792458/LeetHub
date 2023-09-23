class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        word_set = set(words)
        
        memo = dict()
        
        for word in words:
            memo[word] = 1
            
            for i in range(len(word)):
                new_word = word[0:i] + word[i+1:]
                if new_word not in word_set: continue
                if new_word in memo:
                    memo[word] = max(memo[word],memo[new_word]+1)
        
        return max(memo[w] for w in words)