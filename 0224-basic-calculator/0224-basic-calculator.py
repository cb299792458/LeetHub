class Solution:
    def calculate(self, s: str) -> int:
        res=0
        num=0
        sign=1
        stack=[sign]
        
        for c in s:
            if c==' ':
                pass
            elif c.isdigit():
                num = num*10 + int(c)
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            else:
                res+=num*sign
                sign = stack[-1] if c=='+' else -stack[-1]
                num=0
            
        res+=num*sign
        return res