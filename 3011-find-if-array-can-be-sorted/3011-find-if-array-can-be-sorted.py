class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # def bit_count(num):
        #     bits = 0
        #     while num:
        #         bits += num%2
        #         num //= 2
        #     return bits
        
        curr_bits = 0
        last_high = 0
        curr_high = 0
        
        for num in nums:
            bits = num.bit_count()
                        
            if bits == curr_bits:
                curr_high = max(num, curr_high)
            else:
                last_high = curr_high
                curr_high = num
                curr_bits = bits
            if num<last_high:
                return False
        
        return True