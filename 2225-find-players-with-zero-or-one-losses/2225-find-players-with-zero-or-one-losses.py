class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        undefeated, lost_once, trash = set(), set(), set()
        
        for [winner, loser] in matches:
            if winner not in undefeated and winner not in lost_once and winner not in trash:
                undefeated.add(winner)
            if loser in trash:
                pass
            elif loser in lost_once:
                lost_once.remove(loser)
                trash.add(loser)
            else:
                undefeated.discard(loser)
                lost_once.add(loser)
        
        return map(sorted,map(list,[undefeated,lost_once]))