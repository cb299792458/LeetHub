# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        
        def helper(node):
            if node.val>p_val and node.val>q_val:
                return helper(node.left)
            if node.val<p_val and node.val<q_val:
                return helper(node.right)
            return node
        
        return helper(root)