class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        for i in range(len(nums)):
            if i<counts[0]:
                nums[i]=0
            elif i<counts[0]+counts[1]:
                nums[i]=1
            else:
                nums[i]=2
            