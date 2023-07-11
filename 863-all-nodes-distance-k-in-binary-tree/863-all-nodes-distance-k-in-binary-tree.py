# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans=[]
        path_to_target=None
        
        # makes a list of all nodes on path from root to target
        def dfs(node, path):
            if not node: return
            copy=path.copy()
            copy.append(node)
            if node==target:
                # print('hit')
                nonlocal path_to_target
                path_to_target=copy
            dfs(node.left,copy)
            dfs(node.right,copy)
        dfs(root,[])
        
        skips = set()
        
        def find_children(node,dist):
            if not node or node in skips: return
            if not dist:
                ans.append(node.val)
                return
            skips.add(node)
            find_children(node.left,dist-1)
            find_children(node.right,dist-1)
        
        # reverse the list, then run helper on each node, reducing k by 1 each time
        path_to_target.reverse()
        for node in path_to_target:
            find_children(node,k)
            k-=1
        
        return ans
                    
                    