class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i=0
        while i < len(nums):
            if not nums[i] in seen:
                seen.add(nums[i])
                i += 1
            else:
                nums.remove(nums[i])
            
                
        print(seen)