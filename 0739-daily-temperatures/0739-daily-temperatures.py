class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = [] # [greater_temp, index]
        for i in range(N-1, -1, -1):
            temp = temperatures[i]
            while stack and stack [-1][0] <= temp: # if current is warmer/closer
                stack.pop() # replace elements in stack with current
            
            if stack:
                res[i] = stack[-1][1] - i
                
            stack.append((temp, i))
            
        return res