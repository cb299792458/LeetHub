# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base Case
        if not p and not q: return True
        if not p or not q: return False
        
        # check p.val == q.val
        if p.val!=q.val: return False
        
        # check isSameTree(p.left,q.left)
        if not self.isSameTree(p.left,q.left): return False
        
        # check isSameTree(p.right,q.right)
        if not self.isSameTree(p.right,q.right): return False
        
        return True