class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res
        
        byDigitSum = defaultdict(list)
        for num in nums:
            byDigitSum[digitSum(num)].append(num)
        
        res = -1
        for nums in byDigitSum.values():
            if len(nums) < 2:
                continue
            
            nums.sort()
            res = max(res, nums[-1] + nums[-2])
        return res
