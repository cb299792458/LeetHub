class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def string_to_minutes(time):
            [hrs, mins] = time.split(':')
            return 60*int(hrs) + int(mins)
        
        timePoints = list(map(string_to_minutes,timePoints))
        timePoints.sort()
        timePoints.append(timePoints[0]+(24*60))
        
        return min(timePoints[i+1]-timePoints[i] for i in range(len(timePoints)-1))