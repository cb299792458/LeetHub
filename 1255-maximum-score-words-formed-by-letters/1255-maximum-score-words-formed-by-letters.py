class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def getScore(c):
            return score[ord(c)-97]
        
        def canMake(word, counts):
            needed = Counter(word)
            for [char, count] in needed.items():
                if count>counts[char]:
                    return False
            return True

        # find the score that can be made from wordIdx with the letters in counts
        def backtrack(wordIdx, counts): 
            if wordIdx == len(words): # reached end of list of words
                return 0    # base score is zero
            
            curr = words[wordIdx]
            
            # the score if we skip the current word
            skip = backtrack(wordIdx+1, counts)
            if not canMake(curr, counts):
                return skip
            
            # the score if we make the current word
            make = 0
            for char in curr:
                make += getScore(char)
                counts[char] -= 1
            make += backtrack(wordIdx+1, counts)
            
            # put the used letters back in counts
            # this is where backtracking gets its name
            for char in curr:
                counts[char] += 1
            
            # return the better score, making/skipping the current word
            return max(skip, make)
        
        return backtrack(0, Counter(letters))