# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = defaultdict(int)
        
        def dfs(node, level):
            if not node:
                return
            sums[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root,1)
        
        sums = sorted(sums.values())
        if len(sums)<k:
            return -1
        return sums[-k]