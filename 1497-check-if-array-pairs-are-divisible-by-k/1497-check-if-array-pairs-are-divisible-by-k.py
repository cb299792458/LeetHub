class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = Counter()
        
        for num in arr:
            num %= k
            partner = k-num
            
            if remainders[partner]:
                remainders[partner]-=1
            else:
                remainders[num]+=1
        
        return all(val==0 or key==0 for key, val in remainders.items())