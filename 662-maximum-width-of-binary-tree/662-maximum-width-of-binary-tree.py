# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxs=[]
        mins=[]
        
        def _traverse(node,index,level):
            if not node: return
            
            if level >= len(maxs):
                maxs.append(index)
                mins.append(index)
            else:
                maxs[level]=max(maxs[level],index)
                mins[level]=min(mins[level],index)
            
            _traverse(node.left,2*index,level+1)
            _traverse(node.right,2*index+1,level+1)
            
        _traverse(root,0,0)

        diffs = [maxs[i]-mins[i] for i in range(len(maxs))]
        return max(diffs)+1
        