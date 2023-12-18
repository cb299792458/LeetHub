class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lowest, low, high, highest = 10**10,10**10,-10**10,-10**10
        
        for num in nums:
            if num < lowest:
                low = lowest
                lowest = num
            elif num < low:
                low = num
                
            if num > highest:
                high = highest
                highest = num
            elif num > high:
                high = num
                
        return (highest*high) - (lowest*low)