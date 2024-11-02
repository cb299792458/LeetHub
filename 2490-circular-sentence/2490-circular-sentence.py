class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        
        for [i, word] in enumerate(words[:-1]):
            if word[-1] != words[i+1][0]:
                return False
        
        return words[-1][-1] == words[0][0]