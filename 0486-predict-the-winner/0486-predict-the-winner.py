class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def score(l,r):
            if l==r:
                return nums[l]
            take_l = nums[l]-score(l+1,r)
            take_r = nums[r]-score(l,r-1)
            
            return max(take_l,take_r)
        
        return score(0,len(nums)-1)>=0