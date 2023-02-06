class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i%2==0:
                res.append(nums[(i//2)])
            else:
                res.append(nums[n+(i//2)])
            
        return res