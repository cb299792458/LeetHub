class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        # factorial w/ memo
        facts = [1]
        def fact(n):
            while len(facts)<=n: facts.append(facts[-1]*len(facts))
            return facts[n]
        
        def find_ways(nums):
            if len(nums)==0: return 1
            
            root=nums[0]
            left=[]
            right=[]
            for i,n in enumerate(nums):
                if not i: continue
                if n<root: left.append(n)
                else: right.append(n)
            # nCr = n!/(r!(n-r)!)
            return find_ways(left)*find_ways(right)*fact(len(left)+len(right)) // (fact(len(left))*fact(len(right)))
        
        return find_ways(nums) % (10**9 + 7) - 1
                