class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped =[]
        for i, num in enumerate(nums):
            string = ''
            for char in str(num):
                string += str(mapping[int(char)])
            mapped.append((int(string), i, num))
        
        mapped.sort()
        return [m[2] for m in mapped]