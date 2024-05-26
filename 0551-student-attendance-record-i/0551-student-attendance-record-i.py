class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        lates = 0
        for char in s:
            if char == "L":
                lates += 1
                if lates == 3:
                    return False
            else:
                lates = 0
            if char == "A":
                absents += 1
                if absents == 2:
                    return False
        return True