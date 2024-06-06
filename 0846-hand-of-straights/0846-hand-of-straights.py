class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        hand.sort()
        
        for start in hand:
            if not counts[start]:
                continue
            
            for change in range(groupSize):
                if not counts[start+change]:
                    return False
                counts[start+change] -= 1
        
        return True