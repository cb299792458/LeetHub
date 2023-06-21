class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        def find_cost(target):
            res=0
            for num,cost in zip(nums,costs):
                res+=abs(num-target)*cost
            return res

        l,r = min(nums),max(nums)
        
        while l<r:
            m = l + (r-l)//2
            if find_cost(m)<find_cost(m+1):
                r=m
            else: l=m+1
        
        return find_cost(l)
        