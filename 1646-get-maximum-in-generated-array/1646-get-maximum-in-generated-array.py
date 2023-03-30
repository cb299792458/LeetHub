class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: return 0
        
        nums = [0,1]
        biggest = 1
        for i in range(2,n+1):
            if i%2==0:
                nums.append(nums[i//2])
            else:
                new_num = nums[i//2] + nums[(i//2) + 1]
                nums.append(new_num)
                biggest = max(biggest,new_num)
        
        return biggest