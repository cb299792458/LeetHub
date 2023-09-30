class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        smallest=nums[0]
        
        for n in nums:
            while stack and stack[-1][0]<n:
                stack.pop()
                
            if stack:
                (large,small)=stack[-1]
                if small<n<large:
                    return True
            
            stack.append((n,smallest))
            smallest = min(smallest,n)
            
        return False