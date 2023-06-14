# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums=[]
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
            
        dfs(root)
        res=float('inf')
        for i in range(len(nums)-1):
            res=min(res,nums[i+1]-nums[i])
        return res