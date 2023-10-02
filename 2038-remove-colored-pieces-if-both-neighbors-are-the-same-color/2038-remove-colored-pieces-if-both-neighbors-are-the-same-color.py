class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        turns = defaultdict(int)
        
        curr_char = 'C'
        curr_len = 0
        
        for c in colors:
            if c==curr_char:
                curr_len+=1
                
                if curr_len>2:
                    turns[c]+=1
            else:
                curr_char=c
                curr_len=1
        
        return turns['A']>turns['B']