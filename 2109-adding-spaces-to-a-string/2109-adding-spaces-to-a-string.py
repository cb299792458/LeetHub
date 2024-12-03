class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chars = []
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                chars.append(' ')
            chars.append(s[i])
        return ''.join(chars)