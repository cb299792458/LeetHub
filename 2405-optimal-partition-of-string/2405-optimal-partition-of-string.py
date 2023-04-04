class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count=1
        for c in s:
            print(seen)
            if c in seen:
                count+=1
                seen = set()
            seen.add(c)
        return count
                    