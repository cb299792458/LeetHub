class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = [0] * (len(triangle)+1)
        for row in triangle[::-1]:
            curr = []
            for i,num in enumerate(row):
                curr.append( num + min(prev[i], prev[i+1]) )
            prev = curr
        return prev[0]