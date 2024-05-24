class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        memo = defaultdict(list)
        memo[0] = ['']
        
        """
        memo[i] is a list of all "sentences" made of words in wordDict
        that can be formed by breaking up s[0:i] (s from index 0 to i)
        after the memo has been filled, the answer will be memo[N]
        
        Example:
        s = "catsanddog"
        wordDict = ["cat","cats","and","sand","dog"]
        
        s[0:7] = "catsand"
        memo[7] = ["cats and", "cat sand"]
        memo[6] = []
        ...
        memo[10] = ["cats and dog", "cat sand dog"]
        catsand dog
        """
        
        for i in range(N):
            for word in wordDict:
                j = i + len(word)
                if s[i:j] == word: 
                    for sentence in memo[i]:
                        memo[j].append((sentence + ' ' if sentence else '') + word)
        
        return memo[N]