class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        needed = sum(piles)//2
        
        @cache
        def recur(l,r):
            if r-l==1:
                return 0
            
            # alice's turn
            if (r-l)%2:
                # alice takes from beginning
                beg = recur(l+1, r) + piles[l+1]
                # alice takes from end
                end = recur(l, r-1) + piles[r-1]
                return max(beg,end)
            
            # bob's turn
            else:
                # bob takes from beginning
                beg = recur(l+1, r)
                # bob takes from end
                end = recur(l, r-1)
                return min(beg,end)
            
        return recur(-1,len(piles)) > needed
                