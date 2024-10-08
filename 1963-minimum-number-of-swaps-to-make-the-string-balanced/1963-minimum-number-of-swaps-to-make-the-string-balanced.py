class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unmatched = 0
        
        for c in s:
            match c:
                case '[':
                    stack.append(c)
                case ']':
                    if stack:
                        stack.pop()
                    else:
                        unmatched += 1
        
        return (unmatched+1)//2