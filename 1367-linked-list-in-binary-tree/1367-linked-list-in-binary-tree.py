# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def dfs(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            
            return dfs(list_node.next, tree_node.right) or dfs(list_node.next, tree_node.left)
            
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)