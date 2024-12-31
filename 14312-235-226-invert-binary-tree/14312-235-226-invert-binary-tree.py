class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            bfs(node.left)
            bfs(node.right)
            return node
        return bfs(root)