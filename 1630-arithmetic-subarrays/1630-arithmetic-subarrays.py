class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # nums.sort()
        def check(arr):
            arr.sort()
            diff=arr[1]-arr[0]
            for i in range(len(arr)-1):
                if arr[i+1]-arr[i]!=diff:
                    return False
            return True
        
        res = []
        for l_idx, r_idx in zip(l,r):
            res.append(check(nums[l_idx:r_idx+1]))
        return res