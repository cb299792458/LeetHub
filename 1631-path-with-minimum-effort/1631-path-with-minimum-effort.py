class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs=[
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        def possible(effort):
            queue = deque([(0,0)])
            seen = set()
            
            while len(queue):
                (r,c) = queue.popleft()
                seen.add((r,c))
                if r==rows-1 and c==cols-1: return True
                for d in dirs:
                    nr,nc = r+d[0],c+d[1]
                    if nr<0 or nc<0 or nr==rows or nc==cols or (nr,nc) in seen:
                        continue
                    if abs(heights[nr][nc]-heights[r][c]) <= effort:
                        queue.append((nr,nc))
                        seen.add((nr,nc))
            return False
        
        l=0
        # r=max([max(row) for row in heights])
        r=10**6
        while l<r:
            m = l + (r-l)//2
            if(possible(m)):
                r=m
            else:
                l=m+1
        return l