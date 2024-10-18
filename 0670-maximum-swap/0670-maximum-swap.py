class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        num = str(num)
        N = len(num)
        big = N-1
        for i in range(N-2,-1,-1): # go backwards
            if int(num[i])>int(num[big]):
                big = i # save idx of biggest digit
            elif int(num[i])<int(num[big]): # swap digits and save res
                res = int(num[:i] + num[big] + num[i+1:big] + num[i] + num[big+1:])
        
        return res