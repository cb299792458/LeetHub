class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def get_list(index):
            if index<len(grid):
                return grid[index]
            else:
                res=[]
                for row in range(len(grid)):
                    res.append(grid[row][index-len(grid)])
                return res

        ans=0
        for i in range(len(grid)):
            for j in range(len(grid),len(grid)*2):
                if get_list(i)==get_list(j): ans+=1
        return ans