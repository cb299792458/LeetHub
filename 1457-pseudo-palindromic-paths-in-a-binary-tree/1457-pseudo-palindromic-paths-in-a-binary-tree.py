# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = 0
        
        def check(counter):
            odds = sum([c%2 for c in counter.values()])
            return 1 if odds <= 1 else 0
        
        def dfs(node, counter):
            counter[node.val] += 1
            
            if not node.left and not node.right:
                nonlocal paths
                paths += check(counter)
                return
                        
            if node.left:
                dfs(node.left, counter.copy())
            if node.right:
                dfs(node.right, counter.copy())
        
        dfs(root, Counter())
        return paths