class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        l=-1
        r=n
        curr=0
        count=-1
        
        while curr < x and r>0:
            r-=1
            curr+=nums[r]
        if curr==x:
            count = r-l
        
        
        while l<n-1:
            l+=1
            curr+=nums[l]
            
            while curr>x and r<n:
                curr-=nums[r]
                r+=1
                
            if curr==x and l!=r:
                count = max(count, r-l)
                
        return n-count+1 if count!=-1 else count
            