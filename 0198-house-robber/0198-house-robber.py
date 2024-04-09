class Solution:
    def rob(self, nums: List[int]) -> int:
        stole = didnt = 0
        for num in nums:
            temp = stole
            stole = didnt + num
            didnt = max(temp, didnt)
        
        return max(stole, didnt)