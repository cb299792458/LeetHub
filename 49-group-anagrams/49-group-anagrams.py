class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(s):
            return ''.join(sorted(list(s)))
        
        d=defaultdict(list)
        for s in strs:
            d[count(s)].append(s)
            
        return list(d.values())