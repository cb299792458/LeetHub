# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(node):
            if not node:
                return 0
            height = max(find_height(node.left),find_height(node.right)) + 1
            node.height = height
            return height
        find_height(root)
        
        def check_balance(node):
            if not node:
                return True
            if not node.left and not node.right:
                return True
            if node.left and not node.right:
                return node.left.height < 2
            if node.right and not node.left:
                return node.right.height < 2
            
            if abs(node.left.height - node.right.height) > 1:
                return False
            return check_balance(node.left) and check_balance(node.right)
        
        return check_balance(root)