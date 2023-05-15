class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[]
        
        heights = heights + [0]
        for i in range(len(heights)):
            w=0
            while stack and stack[-1]>heights[i]:
                w+=1
                h=stack.pop()
                res = max(res,w*h)
                
            while w+1:
                stack.append(heights[i])
                w-=1
                
                
        return res