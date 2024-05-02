"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones_by_val = {}
        
        def clone(node):
            if not node: return None
            if node.val in clones_by_val:
                return clones_by_val[node.val]
            
            new_clone = Node(node.val, [])
            clones_by_val[node.val] = new_clone
            for n in node.neighbors:
                new_clone.neighbors.append(clone(n))

            return new_clone
        
        return clone(node)
        