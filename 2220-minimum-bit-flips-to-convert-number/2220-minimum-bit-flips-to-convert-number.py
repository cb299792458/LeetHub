class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        
        while len(start)<len(goal):
            start = '0' + start
        while len(start)>len(goal):
            goal = '0' + goal
        
        return sum(int(start[i]!=goal[i]) for i in range(len(start)))