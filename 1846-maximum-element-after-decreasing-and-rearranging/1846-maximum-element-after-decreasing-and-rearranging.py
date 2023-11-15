class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        for num in arr:
            if num>=ans+1:
                ans+=1
                
        return ans