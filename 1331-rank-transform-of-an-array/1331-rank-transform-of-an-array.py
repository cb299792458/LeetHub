class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranked = sorted(set(arr))
        indices = {num: i for [i,num] in enumerate(ranked)}
        
        return [indices[num]+1 for num in arr]