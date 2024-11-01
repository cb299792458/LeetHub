class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack)>=2 and stack[-1]==stack[-2]==c:
                pass
            else:
                stack.append(c)
        return ''.join(stack)