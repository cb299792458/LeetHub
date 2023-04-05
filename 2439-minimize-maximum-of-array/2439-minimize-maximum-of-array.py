class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(arr,n):
            for i in reversed(range(1,len(arr))):
                # while arr[i]>n:
                #     arr[i]-=1
                #     arr[i-1]+=1
                if arr[i]>n:
                    arr[i-1]+=arr[i]-n
                    arr[i]=n
            return arr[0]<=n
                
        # # linear search
        # for j in reversed(range(max(nums))):
        #     if not check(nums.copy(),j): return j+1
        
        
        # binary search
        
        l,r=0,max(nums)
        while l<r :
            m=(l+r)//2
            if check(nums.copy(),m):
                r=m
            else:
                l=m+1
        return l