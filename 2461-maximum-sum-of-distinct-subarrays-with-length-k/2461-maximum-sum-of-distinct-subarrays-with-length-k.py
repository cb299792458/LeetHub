class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = dict()
        curr = best = 0
        s = 0
        for [e, num] in enumerate(nums):
            curr += num
            
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            
            if e-s+1 == k:
                if len(counts) == k:
                    best = max(best, curr)
            
                curr -= nums[s]
                counts[nums[s]] -= 1
                if not counts[nums[s]]:
                    del counts[nums[s]]
                
                s += 1
        
        return best