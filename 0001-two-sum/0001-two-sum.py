class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = sorted(nums)
        left,right = 0,len(nums)-1
        while left<right:
            
            if copy[left] + copy[right] == target:
                break
            elif copy[left] + copy[right] > target:
                right -= 1
            else:
                left += 1
        first = nums.index(copy[left])
        second = nums.index(copy[right])
        if(first==second):
            second = nums.index(copy[right],first+1)
        return [first,second]