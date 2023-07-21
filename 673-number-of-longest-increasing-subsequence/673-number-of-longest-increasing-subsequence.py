class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lengths=[1]*n
        paths=[1]*n
        
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if lengths[j]+1>lengths[i]:
                        lengths[i]=lengths[j]+1
                        paths[i]=paths[j]
                    elif lengths[j]+1==lengths[i]:
                        paths[i]+=paths[j]
        
        max_length=max(lengths)
        
        answer=0
        for k in range(n):
            if lengths[k]==max_length: answer+=paths[k]
                
        print(lengths)
        print(paths)
        return answer