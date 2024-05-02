# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []
        
        while q:
            new_q = []
            level = []
            for node in q:
                if not node: continue
                level.append(node.val)
                new_q.append(node.left)
                new_q.append(node.right)
            res.append(level)
            q = new_q
        
        return res[:-1]