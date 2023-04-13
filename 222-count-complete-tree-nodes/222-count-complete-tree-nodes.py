
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def l_height(node):
            height=0
            while node:
                height+=1
                node=node.left
            return height
        def r_height(node):
            height=0
            while node:
                height+=1
                node=node.right
            return height
        
        l,r=l_height(root),r_height(root)
        
        if l==r: return 2**l-1
        else: return 1+self.countNodes(root.left)+self.countNodes(root.right)