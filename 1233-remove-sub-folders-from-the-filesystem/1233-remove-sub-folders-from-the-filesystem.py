class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        
        res = [folders[0]]
        for folder in folders[1:]:
            if not folder.startswith(res[-1]+'/'):
                res.append(folder)
        
        return res