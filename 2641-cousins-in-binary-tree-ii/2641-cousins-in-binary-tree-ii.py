# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = defaultdict(int)
        
        def fill_level_sums(node, level):
            if not node:
                return
            level_sums[level] += node.val
            fill_level_sums(node.left, level+1)
            fill_level_sums(node.right,level+1)
        fill_level_sums(root,1)
        
        def dfs(node, siblings_sum, level):
            if not node:
                return
            node.val = level_sums[level] - siblings_sum
            
            children_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            dfs(node.left , children_sum, level+1)
            dfs(node.right, children_sum, level+1)
        dfs(root,root.val,1)
        
        return root