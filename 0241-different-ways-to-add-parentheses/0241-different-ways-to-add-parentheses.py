class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        stack = []
        for char in expression:
            if char.isdigit():
                if stack and isinstance(stack[-1],int):
                    stack[-1] = stack[-1]*10 + int(char)
                else:
                    stack.append(int(char))
            else:
                stack.append(char)
        
        cache = {}
        
        def helper(stack):
            if len(stack)==1:
                return stack
            
            key = ''.join([str(s) for s in stack])
            if key in cache:
                return cache[key]
            
            results = []
            
            for [i,c] in enumerate(stack):
                if c=='+' or c=='*' or c=='-':
                    lefts = helper(stack[:i])
                    rights = helper(stack[i+1:])
                    for l in lefts:
                        for r in rights:
                            if c=='+':
                                results.append(l+r)
                            if c=='*':
                                results.append(l*r)
                            if c=='-':
                                results.append(l-r)
            cache[key]=results
            return results
        
        return helper(stack)
                