class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N
        
        if k>0:
            replace = sum(code[1:k+1])
            for i in range(N):
                res[i] = replace
                replace -= code[(i+1)%N]
                replace += code[(i+1+k)%N]
        elif k<0:
            replace = sum(code[k:])
            for i in range(N):
                res[i] = replace
                replace -= code[(k+i)%N]
                replace += code[i%N]
        
        return res