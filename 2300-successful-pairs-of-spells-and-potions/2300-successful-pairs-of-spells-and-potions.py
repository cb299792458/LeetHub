class Solution:    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def left_bisect(spell,success):
            l = 0
            r = len(potions)
            while l < r:
                m = (l+r)//2
                if spell * potions[m] < success:
                    l = m + 1
                else:
                    r = m
            return len(potions) - l
        
        pairs = []
        
        for spell in spells:
            pairs.append(left_bisect(spell,success))
            
        return pairs