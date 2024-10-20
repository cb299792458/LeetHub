class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for c in expression:
            if c==')':
                sub_exp = []
                while stack[-1]!='(':
                    sub_exp.append(stack.pop())
                stack.pop() # remove '('
                op = stack.pop() # get !, &, or |
                
                match op:
                    case '!':
                        stack.append('t' if sub_exp[0]=='f' else 'f')
                    case '&':
                        stack.append('t' if all(c=='t' for c in sub_exp) else 'f')
                    case '|':
                        stack.append('t' if any(c=='t' for c in sub_exp) else 'f')
            elif c!=',':
                stack.append(c)
        assert(len(stack)==1)
        return stack==['t']