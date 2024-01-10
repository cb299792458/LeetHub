# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node:
                return curr
            curr = 10*curr + node.val
            
            if not node.left:
                return dfs(node.right, curr)
            if not node.right:
                return dfs(node.left, curr)
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root,0)