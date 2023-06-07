from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        counts=Counter(nums)
        
        def backtrack(arr,curr_counts=Counter()):
            if len(arr)==len(nums):
                res.append(arr)
                return
            
            for i in range(len(nums)):
                curr_num = nums[i]
                if i>0 and nums[i]==nums[i-1]: continue
                if counts[curr_num]==curr_counts[curr_num]: continue
                    
                curr_counts[curr_num]+=1
                backtrack(arr+[curr_num], curr_counts)
                curr_counts[curr_num]-=1
        
        backtrack([])
        return res
            
            