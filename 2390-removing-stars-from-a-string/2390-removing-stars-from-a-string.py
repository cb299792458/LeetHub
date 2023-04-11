class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        
        for c in s:
            if c!='*':
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
    
    