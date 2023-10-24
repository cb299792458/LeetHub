# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        maxes=[]
        q=[root]
        
        while len(q):
            maxes.append(max([node.val for node in q]))
            newq=[]
            for node in q:
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)
            
            q=newq
        return maxes
        