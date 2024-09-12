class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        consistent = 0
        for word in words:
            flag = True
            for char in word:
                if char not in allowed:
                    flag = False
                    break
            consistent += int(flag)
        return consistent
    