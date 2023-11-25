class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N=len(nums)
        prefix=[]
        suffix=[]
        l,r=0,0
        
        for i in range(N):
            l+=nums[i]
            prefix.append(l)
            
            r+=nums[-1-i]
            suffix.append(r)
            
        suffix=suffix[::-1]
        result = []
        
        for i in range(N):
            n=nums[i]
            curr=0
            
            # diffs on left
            curr+=i*n
            if i>0: curr-=prefix[i-1]
            
            # diffs on right
            curr-=(N-1-i)*n
            if i<N-1: curr+=suffix[i+1]
                
            result.append(curr)
            
        return result