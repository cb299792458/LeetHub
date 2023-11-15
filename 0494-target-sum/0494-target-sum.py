class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums) # 5
        # A 2D memo...
        # memo[index][current] = ways
        memo = [defaultdict(int) for _ in range(N+1)]
        memo[0][0] = 1
        """
        defaultdict(callback)
        a dict(), or hashmap, with the return of callback as its default value
        
        let myObj = {}
        myObj['key'] ++
        doesn't work in JS, but you could...
        
        if (!('key' in myDict)) {
            myObj['key'] = default
        } \\ or...
        
        myObj['key'] ||= default
        """
        
        # index = index in nums, also count of numbers that have been passed so far
        # current = current sum of all numbers passed so far
        # ways = number of paths to reach current after index numbers
        
        for index in range(N):
            num = nums[index]
            for [current,ways] in memo[index].items():
                memo[index+1][current+num] += ways 
                memo[index+1][current-num] += ways 
        
        return memo[N][target]