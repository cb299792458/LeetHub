class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        # print(counts)
        res = []
        changed.sort()
        for num in changed:
            if num==0 and counts[num]:
                res.append(num)
                counts[num]-=2
            if counts[num] and counts[num*2]:
                res.append(num)
                counts[num]-=1
                counts[num*2]-=1
            elif counts[num] and num%2==1: return []

        return res if len(res) == len(changed)/2 else []