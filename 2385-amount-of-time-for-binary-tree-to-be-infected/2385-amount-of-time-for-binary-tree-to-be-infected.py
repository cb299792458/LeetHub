# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjs = defaultdict(list)
        def dfs(node):
            if node.left:
                adjs[node.val].append(node.left.val)
                adjs[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adjs[node.val].append(node.right.val)
                adjs[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        
        infected = set([start])
        q = [start]
        time = 0
        
        while(len(infected)<len(adjs.keys())):
            new_q = []
            for node in q:
                for adj in adjs[node]:
                    if adj not in infected:
                        infected.add(adj)
                        new_q.append(adj)
            q = new_q
            time += 1
        return time
        