class Solution:
    def countAndSay(self, n: int) -> str:
        memo=[None,"1"]
        for i in range(2,n+1):
            string=''
            
            count=0
            prev=''
            for j in range(len(memo[-1])+1):
                if j<len(memo[-1]) and memo[-1][j]==prev:
                    count+=1
                else:
                    if prev: string += str(count) + prev
                    count=1
                    if j<len(memo[-1]): prev=memo[-1][j]
            memo.append(string)
        return memo[-1]