class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        fourth = len(arr)//4
        for i,num in enumerate(arr):
            if num==arr[i+fourth]:
                return num
            
            