class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        code = dict()
        for c1, c2 in zip(s,t):
            if c1 not in code:
                code[c1] = c2
            else:
                if code[c1] != c2:
                    return False
        if len(set(code.values())) != len(code.values()):
            return False
        return True