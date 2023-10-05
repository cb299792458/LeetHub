class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [key for [key,val] in counts.items() if val> len(nums)//3]