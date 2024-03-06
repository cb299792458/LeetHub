class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # tuples -> (length, last_number)
        rise = [0, float('-inf')]
        fall = [0, float('inf')]
        
        for num in nums:
            if num > rise[1]:
                new_fall = [rise[0]+1, num]
            if num < fall[1]:
                new_rise = [fall[0]+1, num]
                # print(new_rise)
                
            if num < rise[1]:
                rise[1] = num
                
            if num > fall[1]:
                fall[1] = num
            
            if new_fall and new_fall[0]>fall[0]:
                fall = new_fall
            if new_rise and new_rise[0]>rise[0]:
                rise = new_rise
            # print(rise,fall)
                
        return max(fall[0],rise[0])