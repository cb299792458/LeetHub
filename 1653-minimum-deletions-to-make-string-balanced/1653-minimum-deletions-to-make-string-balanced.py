class Solution:
    def minimumDeletions(self, s: str) -> int:
        deleted = 0
        stack = []
        
        for char in s:
            if char=='a' and stack and stack[-1]=='b':
                stack.pop()
                deleted += 1
            else:
                stack.append(char)
        
        return deleted