class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N=len(image)
        M=len(image[0])
        
        def dfs(r,c,color,prev_color):
            if r<0 or c<0 or r==N or c==M: return
            if image[r][c] != prev_color or image[r][c] == color: return
            
            image[r][c]=color
            dfs(r+1,c,color,prev_color)
            dfs(r-1,c,color,prev_color)
            dfs(r,c+1,color,prev_color)
            dfs(r,c-1,color,prev_color)
            
        prev_color = image[sr][sc]
        dfs(sr,sc,color,prev_color)
        return image