class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        # print(counts)
        res = []
        changed.sort()
        for num in changed:
            if counts[num]:
                if num==0:
                    res.append(num)
                    counts[num]-=2
                elif counts[num*2]:
                    res.append(num)
                    counts[num]-=1
                    counts[num*2]-=1
                else: return []

        return res if len(res) == len(changed)/2 else []