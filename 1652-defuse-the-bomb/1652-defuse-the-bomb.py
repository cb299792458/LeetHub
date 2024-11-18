class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        result = [0] * N
        
        if k>0:
            replacement = sum(code[1:k+1])
            for i in range(N):
                result[i] = replacement
                replacement -= code[(i+1)%N]
                replacement += code[(i+1+k)%N]
        elif k<0:
            replacement = sum(code[k:])
            for i in range(N):
                result[i] = replacement
                replacement -= code[(k+i)%N]
                replacement += code[i%N]
        
        return result