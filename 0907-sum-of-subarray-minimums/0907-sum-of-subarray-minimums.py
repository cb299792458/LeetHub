class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0
        stack = [(-1,float('-inf'))] # idx, num
        for i,n in enumerate(arr+[float('-inf')]):
            while n < stack[-1][1]:
                (j,m) = stack.pop()
                l = j - stack[-1][0]
                r = i - j
                total += l*r*m
            stack.append((i,n))

        return total % (10**9+7)
        
        