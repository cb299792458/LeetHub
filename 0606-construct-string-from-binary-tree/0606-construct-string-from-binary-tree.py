# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        stack=[]
        def dfs(node):
            if not node: return
            stack.append(str(node.val))
            
            if node.left:
                stack.append('(')
                dfs(node.left)
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
            
            if node.right:
                if not node.left:
                    stack.append('()')
                stack.append('(')
                dfs(node.right)
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
            
        dfs(root)
        return ''.join(stack)
