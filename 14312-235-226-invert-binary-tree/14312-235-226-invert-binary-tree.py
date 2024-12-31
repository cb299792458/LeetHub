class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            swap(node.left)
            swap(node.right)
        swap(root)
        return root