# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()
        def dfs(node):
            if not node: return
            counts[node.val]+=1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        by_count = defaultdict(list)
        for val,count in counts.items():
            by_count[count].append(val)
        return by_count[max(by_count.keys())]