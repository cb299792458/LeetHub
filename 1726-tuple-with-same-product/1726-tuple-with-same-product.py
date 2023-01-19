import math
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i]*nums[j]
                if not product in products:
                    products[product] = 0
                products[product] += 1
        
        count = 0
        for key in products:
            if products[key] > 1:
                count += products[key] * (products[key]-1)
            
        return count*4