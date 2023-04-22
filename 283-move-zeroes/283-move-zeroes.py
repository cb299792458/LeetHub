class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                i+=1
                
        
        