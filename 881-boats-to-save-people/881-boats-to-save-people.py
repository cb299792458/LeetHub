class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(key=lambda x: -x)
        l=0
        r=len(people)-1
        count=0
        
        while(l<=r):
            
            if people[r] + people[l] <= limit:
                r -= 1
            l+=1
            
            count+=1
        return count