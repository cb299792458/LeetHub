class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda n: int(''.join(map(lambda d: str(mapping[int(d)]), str(n)))))