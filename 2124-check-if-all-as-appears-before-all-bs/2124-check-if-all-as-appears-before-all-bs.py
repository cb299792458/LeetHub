class Solution:
    def checkString(self, s: str) -> bool:
        hasB = False
        for char in s:
            if char=='b':
                hasB = True
            else:
                if hasB:
                    return False
        return True