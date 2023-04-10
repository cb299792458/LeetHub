class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in dictionary:
                stack.append(c)
            elif stack and c == dictionary[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
        