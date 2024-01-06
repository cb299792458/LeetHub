# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return ''
        
        head = str(root.val)
        left = ' l(' + self.serialize(root.left) + ')' if root.left else ''
        right = ' r(' + self.serialize(root.right) + ')' if root.right else ''
        
        return head + left + right

    def deserialize(self, data):
        if not data: return None
        
        head = TreeNode(int(data.split()[0]))
        if len(data.split())==1: return head
        
        data = data[data.index(' ')+1:]
        
        left,right = '',''
        
        if data[0]=='l':
            i=1
            parens=0
            while parens or i==1:
                if data[i]=='(': parens+=1
                if data[i]==')': parens-=1
                i+=1
            
            left = data[2:i-1]
            
            if i!=len(data): right = data[i+3:-1]
        else: right=data[2:-1]
        
        head.left = self.deserialize(left)
        head.right = self.deserialize(right)
        return head
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))