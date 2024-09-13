class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        curr = 0
        for i in range(len(arr)):
            curr = curr ^ arr[i]
            prefix_xor.append(curr)
        
        return [prefix_xor[s]^prefix_xor[e+1] for [s,e] in queries]