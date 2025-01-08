class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a,b):
            return b[:len(a)] == a and b[-len(a):] == a
        res = 0
        N = len(words)
        for i in range(N):
            for j in range(i+1,N):
                if isPrefixAndSuffix(words[i],words[j]):
                    res += 1
        return res