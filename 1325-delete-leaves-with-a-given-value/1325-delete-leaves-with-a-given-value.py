# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def prune(node):
            if not node:
                return None
            node.left = prune(node.left)
            node.right = prune(node.right)
            
            if not node.left and not node.right and node.val == target:
                node = None
            
            return node
        
        return prune(root)