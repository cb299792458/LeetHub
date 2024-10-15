class Solution:
    def minimumSteps(self, s: str) -> int:
        blacks = 0
        swaps = 0
        for c in s:
            if c=='1':
                # keep track of previous black balls
                blacks += 1
            else:
                # swap all previous black balls past this
                swaps += blacks
        
        return swaps