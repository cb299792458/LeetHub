class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def check(diff):
            pairs=0
            copy=nums.copy()
            while copy:
                curr=copy.pop()
                if copy and curr-copy[-1]<=diff:
                    pairs+=1
                    copy.pop()
            return pairs>=p
        
        l,r=0,nums[-1]-nums[0]
        while l<r:
            m=l+(r-l)//2
            
            if check(m):
                r=m
            else:
                l=m+1
        return l