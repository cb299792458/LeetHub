class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums: return res
        
        start=prev=nums[0]
        nums.append(float('inf'))
        
        for n in nums[1:]:
            if n==prev+1:
                prev=n
            else:
                if prev==start:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(prev))
                start=prev=n
        return res