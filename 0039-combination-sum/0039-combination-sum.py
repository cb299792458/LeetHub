class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def _backtrack(combo,idx):
            if idx > len(candidates)-1: return
            amt=sum(combo)
            if amt>target: return
            if amt==target:
                res.append(combo)
                return
            
            _backtrack([*combo,candidates[idx]],idx)
            _backtrack([*combo],idx+1)
            
        _backtrack([],0)
        return res