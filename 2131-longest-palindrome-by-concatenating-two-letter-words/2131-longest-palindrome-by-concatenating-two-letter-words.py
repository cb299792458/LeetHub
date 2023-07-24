class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length=0
        counts=defaultdict(int)
        
        for word in words:
            a,b=word[0],word[1]
            if counts[b+a]:
                counts[b+a]-=1
                length+=2
            else:
                counts[a+b]+=1
                
        for key,val in counts.items():
            if key[0]==key[1] and val%2:
                return (length+1)*2
        return (length)*2