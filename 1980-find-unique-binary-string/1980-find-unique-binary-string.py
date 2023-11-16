class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        nums = set(nums)
        ans = ''
        def backtrack(s):
            if len(s)==N:
                if s not in nums:
                    nonlocal ans
                    ans = s
                return
            backtrack(s+'0')
            backtrack(s+'1')
        backtrack('')
        return ans