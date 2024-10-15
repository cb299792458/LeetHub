class Solution:
    def minimumSteps(self, s: str) -> int:
        blacks = 0
        swaps = 0
        for c in s:
            if c=='1':
                blacks += 1
            else:
                swaps += blacks
        
        return swaps