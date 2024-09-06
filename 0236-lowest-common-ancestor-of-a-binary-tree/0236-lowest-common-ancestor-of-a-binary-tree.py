# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(node,p,q):
            if not node:
                return False
            if node == p or node == q:
                return node
            
            left_is_common_ancestor = check(node.left,p,q)
            right_is_common_ancestor = check(node.right,p,q)
            
            if left_is_common_ancestor and right_is_common_ancestor:
                return node
            return left_is_common_ancestor or right_is_common_ancestor
        
        return check(root,p,q)