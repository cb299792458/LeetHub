class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        increases = [0]*N
        decreases = [0]*N
        
        for i in range(N-2):
            first = rating[i]
            for j in range(i+1,N-1):
                second = rating[j]
                if second>first:
                    increases[j] += 1
                if second<first:
                    decreases[j] += 1
        
        print(increases, decreases)
        teams = 0
        for j in range(1,N-1):
            second = rating[j]
            for k in range(j+1,N):
                third = rating[k]
                if second<third:
                    teams += increases[j]
                if second>third:
                    teams += decreases[j]
        
        return teams