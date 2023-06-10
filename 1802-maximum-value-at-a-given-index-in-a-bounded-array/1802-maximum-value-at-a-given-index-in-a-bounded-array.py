class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(target):
            minSum = target
            
            # left side
            minSum+=(target*(target-1))//2
            if target<index+1:
                minSum+=index+1-target
            else:
                minSum-=(target-(index+1))*(target-(index+1)+1)//2
            
            # right side
            minSum+=(target*(target-1))//2
            spaces = n-index-1
            if target-1<spaces:
                minSum+=spaces-target+1
            else:
                minSum-=(target-spaces-1)*(target-spaces)//2
                
            return minSum
        
        
        l,r = 1,maxSum
        while l<r:
            m = (r+l+1)//2
            if check(m)<=maxSum:
                l = m
            else: r = m-1
        return l