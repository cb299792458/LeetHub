# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        while l<r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m # r is always bad
            else:
                l = m + 1 # l is good or first bad
        return l