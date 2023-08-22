class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d=dict()
        for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            d[i]=c
            
        stri=''
        while columnNumber:
            columnNumber-=1
            stri = d[columnNumber%26] + stri
            columnNumber = columnNumber//26
            
        return stri