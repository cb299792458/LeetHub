class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        lefts = [0] * N
        right = [0] * N
        
        l=r=1
        for i in range(N):
            lefts[i] = l
            right[N-i-1] = r
            l *= nums[i]
            r *= nums[N-i-1]
        
        return [lefts[i]*right[i] for i in range(N)]