class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return ''
        
        print('S:',s)
        l, r = 0, len(s)-1
        prefix, suffix = '', ''
        while not s[l].isdigit():
            prefix = prefix + s[l]
            l+=1

            # base case
            if l == len(s):
                return prefix
        while not s[r].isdigit() and s[r] != ']':
            suffix = s[r] + suffix
            r -= 1

        k_string = ''
        while s[l].isdigit():
            k_string += s[l]
            l+=1
        k = int(k_string)
        if s[l] != '[': print('non [ after k')
        l+=1
        left_brackets, right_brackets = 1, 0
        substring = ''

        while left_brackets > right_brackets:
            # print(s, l)
            char = s[l]

            if char=='[':
                left_brackets+=1
            elif char==']':
                right_brackets+=1
            substring += char
            l+=1
        print(substring[:-1])
        repeated_substring = k * self.decodeString(substring[:-1])
        
        return prefix + repeated_substring + self.decodeString(s[l:r+1]) + suffix