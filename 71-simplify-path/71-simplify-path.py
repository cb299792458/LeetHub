class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        
        res=[]
        for folder in folders:
            if not folder or folder=='.': continue
            
            if folder=='..':
                if res: res.pop()
            else: res.append(folder)
            
            
        return '/' + '/'.join(res)