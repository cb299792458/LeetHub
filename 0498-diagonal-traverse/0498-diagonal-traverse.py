class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = defaultdict(deque)
        for r,submat in enumerate(mat):
            for c,n in enumerate(submat):
                diag=r+c
                if diag%2:
                    diags[diag].append(n)
                else:
                    diags[diag].appendleft(n)
        res = []
        for i in range(len(mat)+len(mat[0])-1):
            res.extend(diags[i])
        return res