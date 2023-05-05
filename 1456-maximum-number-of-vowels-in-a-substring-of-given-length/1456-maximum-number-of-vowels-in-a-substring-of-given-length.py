class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set(['a','e','i','o','u'])
        res=0
        for c in s[:k]:
            if c in vowels: res += 1
        curr = res
        for i in range(k,len(s)):
            if s[i] in vowels: curr+=1
            if s[i-k] in vowels: curr-=1
            print([i,k,curr])
            res = max(curr,res)
        return res