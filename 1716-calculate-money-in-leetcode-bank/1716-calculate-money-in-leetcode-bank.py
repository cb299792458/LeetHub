class Solution:
    def totalMoney(self, n: int) -> int:
        prev = 6
        total = 0
        for day in range(n):
            if day%7:
                prev += 1
            else:
                prev -= 5
            total += prev
        
        return total