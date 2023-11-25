class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N=len(nums)
        prefix=[None]*N
        suffix=[None]*N
        l,r=0,0
        for i in range(N):
            l+=nums[i]
            prefix[i]=l
            r+=nums[-1-i]
            suffix[-1-i]=r

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