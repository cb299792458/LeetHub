class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res=[]
        total=sum(nums[:2*k])
        
        for i in range(2*k,len(nums)):
            total+=nums[i]
            res.append(total//(2*k+1))
            total-=nums[i-2*k]
            
        # print(res)
        if len(res)==0: return [-1]*len(nums)
        return [-1]*k+res+[-1]*k