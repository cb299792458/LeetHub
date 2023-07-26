class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabet='abcdefghijklmnopqrstuvwxyz'
        indices={c: i for i,c in enumerate(alphabet)}
        # for i,c in enumerate(alphabet):
        #     indices[c]=i
        s_by_idx = [indices[c] for c in s]
        
        deltas = [0 for _ in range(len(s)+1)]
        
        for [s,e,d] in shifts:
            d = d if d else -1
            deltas[s]+=d
            deltas[e+1]-=d
            
        change = 0
        for i in range(len(s_by_idx)):
            change += deltas[i]
            s_by_idx[i]+=change
            
        return ''.join([alphabet[i%26] for i in s_by_idx])