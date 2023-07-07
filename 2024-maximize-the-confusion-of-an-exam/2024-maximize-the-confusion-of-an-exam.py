class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counts={'T':0,'F':0}
        l,r=0,0
        confusion=0
        
        while r<len(answerKey):
            counts[answerKey[r]]+=1
            while min(counts.values())>k:
                counts[answerKey[l]]-=1
                l+=1
            confusion=max(confusion,max(counts.values())+k)
            r+=1
            
            
            
        
        return min(confusion,len(answerKey))
        