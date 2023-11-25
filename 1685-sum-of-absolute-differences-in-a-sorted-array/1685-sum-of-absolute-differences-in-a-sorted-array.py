class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = []
        total = sum(nums)
        
        i = 0
        passed = 0
        coming = total
        
        for n in nums:
            curr = 0
            
            curr += i*n
            curr -= (N-1-i)*n
            i += 1

            curr -= passed
            passed += n
            coming -= n
            curr += coming
        
            result.append(curr)
            
        return result