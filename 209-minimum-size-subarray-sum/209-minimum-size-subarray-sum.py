class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,-1
        total=0
        min_len=float('inf')
        
        while r<len(nums):
            if total<target:
                r+=1
                if r==len(nums): break
                total+=nums[r]
            else:
                l+=1
                total-=nums[l-1]
                
            if total>=target:
                min_len=min(min_len,r-l+1)
                
        return min_len if min_len != float('inf') else 0