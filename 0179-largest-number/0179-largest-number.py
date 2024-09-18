class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            if a+b>b+a:
                return -1
            return 1
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(cmp))
        if nums[0]=='0':
            return '0'
        
        return ''.join(nums)