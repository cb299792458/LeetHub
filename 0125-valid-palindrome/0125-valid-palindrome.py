class Solution:
    def isPalindrome(self, s: str) -> bool:
        # converted = ''
        # for c in s:
        #     if c.isalnum():
        #         converted += c.lower()
                
        converted = [c for c in s.lower() if c.isalnum()]
        
        l,r = 0,len(converted)-1
        while l < r:
            if converted[l] != converted[r]:
                return False
            l += 1
            r -= 1
            
        return True