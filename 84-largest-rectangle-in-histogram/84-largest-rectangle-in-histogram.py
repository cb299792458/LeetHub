class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#         # stack heights, calc all to left when right is smaller
#         res=0
#         stack=[]
        
#         heights = heights + [0]
#         for i in range(len(heights)):
#             w=0
#             while stack and stack[-1]>heights[i]:
#                 w+=1
#                 h=stack.pop()
#                 res = max(res,w*h)
                
#             stack += [heights[i]] * (w+1)
                
#         return res


        # three passes, find indices of lower heights to left and right
        res=0
        heights.append(0)
        next_smaller = [-1 for _ in range(len(heights))]
        prev_smaller = [-1 for _ in range(len(heights))]
        
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
            
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
            
        for i in range(len(heights)):
            height = heights[i]
            width = next_smaller[i] - prev_smaller[i] - 1
            # print(next_smaller[i],prev_smaller[i],width)
            res = max(res,height*width)
        
        return res
        