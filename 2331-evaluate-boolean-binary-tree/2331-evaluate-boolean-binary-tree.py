# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(node):
            if node.val < 2:
                return bool(node.val)
            if node.val == 2:
                return eval(node.left) or eval(node.right)
            if node.val == 3:
                return eval(node.left) and eval(node.right)
        
        return eval(root)