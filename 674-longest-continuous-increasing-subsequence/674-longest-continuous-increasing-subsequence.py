class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        res = 1
        
        for num in nums[1:]:
            if num>subseq[-1]:
                subseq.append(num)
                res=max(res,len(subseq))
            else:
                subseq=[num]
                
        return res