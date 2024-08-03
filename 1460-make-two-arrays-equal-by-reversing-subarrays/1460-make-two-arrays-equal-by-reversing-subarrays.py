class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts1 = Counter(target)
        counts2 = Counter(arr)
        
        for [char, count] in counts1.items():
            if counts2[char] != count:
                return False
            
        return len(counts1.keys()) == len(counts2.keys())