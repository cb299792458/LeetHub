class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        largest_by_end = [[] for _ in nums]
        
        for i in range(len(nums)): # end index
            largest = []
            for j in range(i):   # start index
                if nums[i] % nums[j] == 0:
                    if len(largest_by_end[j]) > len(largest):
                        largest = largest_by_end[j]
            largest_by_end[i] = largest + [nums[i]]
        
        return max(largest_by_end, key=len)