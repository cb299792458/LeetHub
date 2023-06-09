class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r=0,len(letters)-1
        res = letters[0]
        
        while(l<=r):
            m=l+(r-l)//2
            if letters[m]<=target:
                l=m+1
            else:
                res=letters[m]
                r=m-1
        return res