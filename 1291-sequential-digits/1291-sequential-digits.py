class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def recur(num):
            if num > high:
                return
            if num >= low:
                res.append(num)
                
            last = num % 10
            if last != 9:
                recur(10*num + last + 1)
        for i in range(1,10):
            recur(i)
        res.sort()
        return res