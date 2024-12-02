class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for [i, word] in enumerate(sentence.split(' ')):
            if word[:len(searchWord)] == searchWord:
                return i+1
        return -1