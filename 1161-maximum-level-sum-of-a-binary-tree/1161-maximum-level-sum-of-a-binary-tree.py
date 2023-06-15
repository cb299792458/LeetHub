# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        ans = level = 1
        queue = [root]
        
        while queue:
            new_queue = []
            curr_sum = 0
            for node in queue:
                curr_sum+=node.val
                if node.left: new_queue.append(node.left)
                if node.right: new_queue.append(node.right)
            
            if curr_sum>max_sum:
                max_sum=curr_sum
                ans=level
            
            queue = new_queue
            level+=1
        return ans