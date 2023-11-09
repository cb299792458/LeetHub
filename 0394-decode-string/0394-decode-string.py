class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c==']':
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()
                
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k=int(k)
                
                stack.append(k * self.decodeString(substring))
            else: 
                stack.append(c)
                
        return ''.join(stack)
        
#         # recursive 
#         # empty string base case
#         if not s: return ''
        
#         l, r = 0, len(s)-1
#         prefix, suffix = '', ''
#         while not s[l].isdigit():
#             prefix = prefix + s[l]
#             l+=1

#             # all letters base case
#             if l == len(s):
#                 return prefix
#         while not s[r].isdigit() and s[r] != ']':
#             suffix = s[r] + suffix
#             r -= 1

#         k_string = ''
#         while s[l].isdigit():
#             k_string += s[l]
#             l+=1
#         k = int(k_string)

#         l+=1
#         left_brackets, right_brackets = 1, 0
#         substring = '[' # substring includes brackets (for nested case)

#         while left_brackets > right_brackets:
#             char = s[l]

#             if char=='[':
#                 left_brackets+=1
#             elif char==']':
#                 right_brackets+=1
#             substring += char # always add char to substring, even [ or ]
            
#             l+=1
#         # remove first and last chars (always [ and ])
#         repeated_substring = k * self.decodeString(substring[1:-1])
        
#         return prefix + repeated_substring + self.decodeString(s[l:r+1]) + suffix