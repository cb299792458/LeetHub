class Solution:
    def longestValidParentheses(self, substring):
        stack = [(-1,None)]
        longest = 0
        
        for i,c in enumerate(substring):
            if c=='(': # keep track of all left parens
                stack.append((i,c))
            else:
                if stack[-1][1]: # close last left parens
                    stack.pop()
                    if not stack: # allow proper length calculation w/ empty stack
                        stack.append((-1,None)) 
                    longest = max(longest, i - stack[-1][0]) # stack[-1] is now start of valid substring
                else: # start new valid substring
                    stack.append((i,None))
        
        return longest