class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest = ''
        current = ''
        
        for d in num:
            current += d
            if int(d)%2:
                largest = current
        return largest