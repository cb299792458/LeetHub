class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of_num = dict()
        for i,num in enumerate(nums):
            if target - num in index_of_num:
                return [i,index_of_num[target - num]]
            index_of_num[num] = i
        