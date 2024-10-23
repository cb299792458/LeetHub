# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levels = {}
        parent = {}
        
        def dfs(node, l, p):
            if not node:
                return
            levels[node.val] = l
            parent[node.val] = p
            
            dfs(node.left , l+1, node.val)
            dfs(node.right, l+1, node.val)
        
        dfs(root,0,0)
        return levels[x]==levels[y] and parent[x]!=parent[y]