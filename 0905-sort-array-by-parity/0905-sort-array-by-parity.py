class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return sorted(nums,key=lambda x:x%2)
        o = [n for n in nums if n%2]
        e = [n for n in nums if not n%2]
        return e+o