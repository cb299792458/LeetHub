class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        
        @cache
        def match(si,pi):
            if pi==P:
                return si==S
            if si==S:
                return all(c=='*' for c in p[pi:])
            
            if p[pi]=='*':
                return match(si,pi+1) or match(si+1,pi)
                #      wild = ''         wild = next char or more
            
            elif p[pi]=='?':
                return match(si+1,pi+1)
            else:
                if p[pi]==s[si]:
                    return match(si+1,pi+1)
                else:
                    return False
        
        return match(0,0)