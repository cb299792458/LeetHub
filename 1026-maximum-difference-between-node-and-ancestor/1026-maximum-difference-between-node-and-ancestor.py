# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def search(node, small, large):
            if not node: return
            
            self.ans = max(self.ans, node.val-small, large-node.val)
            small = min(small, node.val)
            large = max(large, node.val)
            
            search(node.left, small, large)
            search(node.right, small, large)
        
        search(root, float('inf'), -float('inf'))
        return self.ans