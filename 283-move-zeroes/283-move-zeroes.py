class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(len(nums)):
            # print(nums,i,j)
            if nums[j]==0:
                # j+=1
                pass
            else:
                nums[i],nums[j]=nums[j],nums[i]
                # j+=1
                i+=1
                
        
        