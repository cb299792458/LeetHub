class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        def combine(s1,s2):
            if not s1 or not s2:
                return s1 or s2
            return s1 + ' ' + s2

        ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        
        billions = num // 1000000000
        num %= 1000000000
        millions = num // 1000000
        num %= 1000000
        thousands = num // 1000
        num %= 1000
        hundreds = num // 100
        num %= 100
        
        res = ''
        if num<20:
            res = ones[num]
        else:
            res = combine(tens[num//10],ones[num%10])
        
        if hundreds:
            res = combine(ones[hundreds] + ' Hundred', res)
        if thousands:
            res = combine(self.numberToWords(thousands) + ' Thousand', res)
        if millions:
            res = combine(self.numberToWords(millions) + ' Million', res)
        if billions:
            res = combine(self.numberToWords(billions) + ' Billion', res)
        
        return res