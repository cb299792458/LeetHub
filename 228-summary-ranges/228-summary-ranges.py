class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums: return res
        
        start=prev=nums[0]
        nums.append(float('inf'))
        
        for i,n in enumerate(nums):
            if not i: continue
            if n==prev+1:
                prev+=1
            else:
                if prev==start:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(prev))
                start=prev=n
        return res