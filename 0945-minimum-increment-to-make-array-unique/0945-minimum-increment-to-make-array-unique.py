class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
        
        for i in range(1,len(nums)):
            num = nums[i]
            if num<=nums[i-1]:
                new = nums[i-1]+1
                moves += new - num
                nums[i] = new
        
        return moves