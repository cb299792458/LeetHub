class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        chars = set()
        longest = 0
        
        while r < len(s):
            if not s[r] in chars:
                chars.add(s[r])
                r+=1
                longest = max(longest, r-l)
            else:
                chars.remove(s[l])
                l+=1

        return longest