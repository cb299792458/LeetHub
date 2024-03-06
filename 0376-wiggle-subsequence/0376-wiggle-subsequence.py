class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # tuples -> (length, last_number)
        rise = [0, float('-inf')]
        fall = [0, float('inf')]
        
        for num in nums:
            # add num at end and switch
            if num > rise[1]:
                new_fall = [rise[0]+1, num] # i had rise and fall reversed here
            if num < fall[1]:
                new_rise = [fall[0]+1, num] # for like half an hour T_T
            
            # replace end w/ num (no switch)
            if num < rise[1]:
                rise[1] = num
            if num > fall[1]:
                fall[1] = num
            
            # take best answers to next iteration
            if new_fall and new_fall[0]>fall[0]:
                fall = new_fall
            if new_rise and new_rise[0]>rise[0]:
                rise = new_rise
                
        return max(fall[0],rise[0])