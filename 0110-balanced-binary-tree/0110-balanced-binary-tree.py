# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_heights(node):
            if not node:
                return 0
            height = max(find_heights(node.left), find_heights(node.right)) + 1
            node.height = height
            return height
        
        find_heights(root)
        
        def check_balance(node) -> bool:
            if not node: # node doesn't exist
                return True
            
            if not node.left and not node.right: # node's children don't exist
                return True
            
            if node.left and not node.right: # one child doesn't exist
                return node.left.height == 1
            
            if node.right and not node.left: # one child doesn't exist
                return node.right.height == 1
                
            if abs(node.right.height - node.left.height) >= 2:
                return False
            
            return check_balance(node.left) and check_balance(node.right)
        
        return check_balance(root)