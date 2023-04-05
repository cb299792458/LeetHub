class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(n):
            arr=nums.copy()
            for i in reversed(range(1,len(arr))):
                if arr[i]>n:
                    arr[i-1]+=arr[i]-n
                    arr[i]=n
            return arr[0]<=n
                
        # # linear search
        # for j in reversed(range(max(nums))):
        #     if not check(nums.copy(),j): return j+1
        
        
        # # binary search
        l,r=0,max(nums)
        while l<r :
            m=(l+r)//2
            if check(m):
                r=m
            else:
                l=m+1
        return l