class Solution:
    def findComplement(self, num: int) -> int:
        def binary_string(num):
            res = ''
            while num:
                res = str(num%2) + res
                num //= 2
            return res
        
        bs = binary_string(num)
        complement = 0
        for c in bs:
            complement *= 2
            complement += int(c=='0')
        return complement