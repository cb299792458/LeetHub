class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        
        def fill(r,c,prev):
            if r<0 or c<0 or r==m or c==n:
                return
            if image[r][c] == color:
                return
            if image[r][c] != prev:
                return
            
            image[r][c] = color
            
            fill(r+1,c,prev)
            fill(r-1,c,prev)
            fill(r,c+1,prev)
            fill(r,c-1,prev)
            
        prev = image[sr][sc]
        fill(sr,sc,prev)
        
        return image