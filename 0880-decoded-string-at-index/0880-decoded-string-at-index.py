class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        letters = set(chr(ord('a')+i) for i in range(26))
        
        count=0
        stack=deque()
        for c in s:
            if c in letters:
                count+=1
            else:
                count*=int(c)
            stack.append(c)
            if count>=k: break
                
        while stack:
            c = stack.pop()
            if c not in letters:
                count//=int(c)
                k%=count
            else:
                if count==k or k==0: return c
                count-=1
                
