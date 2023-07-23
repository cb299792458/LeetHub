# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp=defaultdict(list)
        dp[1]=[TreeNode(0)]
        dp[3]=[TreeNode(0,TreeNode(0),TreeNode(0))]
        
        for i in range(5,n+2,2):
            for l in range(1,i,2):
                r=i-l-1
                for left in dp[l]:
                    for right in dp[r]:
                        dp[i].append(TreeNode(0,left,right))
        return dp[n]