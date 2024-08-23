class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []
        sign = 1
        num = ''
        
        for c in expression:
            if c=='/':
                numerators.append(sign*int(num))
                num = ''
                sign = 1
            elif c=='-':
                if num:
                    denominators.append(sign*int(num))
                    num = ''
                sign = -1
            elif c=='+':
                denominators.append(sign*int(num))
                num = ''
            else:
                num += c
        denominators.append(sign*int(num))
        
        top = 0
        bot = 1
        for n in denominators:
            bot *= n
        for i,n in enumerate(numerators):
            top += n*bot//denominators[i]
        return f"{top//math.gcd(top,bot)}/{bot//math.gcd(top,bot)}"
                