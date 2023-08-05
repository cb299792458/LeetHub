# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = dict()
        
        def helper(start,end):
            if start>end:
                return [None]
            if (start,end) in memo:
                return memo[(start,end)]
            
            possibilities=[]
            for root in range(start,end+1):
                lefts = helper(start,root-1)
                rights = helper(root+1,end)
                for l in lefts:
                    for r in rights:
                        possibilities.append(TreeNode(root,l,r))
            memo[(start,end)]=possibilities
            return possibilities
        
        return helper(1,n)