class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        word1=[c for c in word1][::-1]
        word2=[c for c in word2][::-1]
        while word1 and word2:
            res += word1.pop() + word2.pop()
            
        return res + ''.join(word1[::-1]+word2[::-1])