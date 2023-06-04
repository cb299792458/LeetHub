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
            
        
#         stack = []
        
#         i=-1
#         while i<len(s)-1:
#             i+=1
#             if s[i]==' ': continue
#             if s[i]=='(':
#                 parens=1
#                 j=i+1
                
#                 while parens:
#                     if s[j]=='(': parens+=1
#                     if s[j]==')': parens-=1
#                     j+=1
                
#                 stack.append(self.calculate(s[i+1:j-1]))
#                 i=j-1
#             elif s[i].isdigit():
#                 temp=s[i]
#                 while i<len(s)-1 and s[i+1].isdigit():
#                     temp+=s[i+1]
#                     i+=1
#                 stack.append(int(temp))
#             else: stack.append(s[i])
                
#         # print(stack)
#         res=0
#         sign=1
        
#         for curr in stack:
#             if curr=='-':
#                 sign=-1
#             elif curr=='+':
#                 pass
#             else:
#                 res+=sign*curr
#                 sign=1
#         return res
            
            
            