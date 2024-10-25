class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort(key=len)
        
        res = []
        for folder in folders:
            if not any(folder.startswith(r+'/') for r in res):
                res.append(folder)
        
        return res