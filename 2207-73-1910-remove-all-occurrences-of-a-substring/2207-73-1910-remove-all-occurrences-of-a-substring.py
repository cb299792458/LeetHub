class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        stack = []
        N = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= N and stack[-N:] == part:
                for _ in range(N):
                    stack.pop()
        
        return ''.join(stack)