class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations=[]
        
        def backtrack(num,nums):
            if len(nums)==k:
                combinations.append(nums)
                return
            if num>n:
                return
            
            backtrack(num+1,nums[:])
            nums.append(num)
            backtrack(num+1,nums[:])
            
        backtrack(1,[])
        return combinations