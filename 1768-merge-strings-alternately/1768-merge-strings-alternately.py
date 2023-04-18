class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        i=0
        while i<min(len(word1),len(word2)):
            res+=word1[i]+word2[i]
            i+=1
        return res + word1[i:]+word2[i:]