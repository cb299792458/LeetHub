class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        for [w,l] in matches:
            losses[l] += 1
            losses[w] += 0
        
        return [
            sorted([p for p,c in losses.items() if c==0]),
            sorted([p for p,c in losses.items() if c==1]),
            
        ]