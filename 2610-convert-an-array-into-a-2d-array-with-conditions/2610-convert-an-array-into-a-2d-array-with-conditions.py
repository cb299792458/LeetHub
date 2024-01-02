class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        result = []
        while counts:
            new_counts = Counter()
            row = []
            for num, count in counts.items():
                row.append(num)
                if count>1:
                    new_counts[num] = count-1
            counts = new_counts
            result.append(row)
        return result
            