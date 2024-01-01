class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi=0
        content=0
        for cookie in s:
            if gi<len(g) and cookie>=g[gi]:
                content+=1
                gi+=1
        return content