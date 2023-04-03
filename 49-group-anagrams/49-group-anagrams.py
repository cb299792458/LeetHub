class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_chars(s):
            return ''.join(sorted(list(s)))
        
        d=defaultdict(list)
        for s in strs:
            d[sort_chars(s)].append(s)
            
        return list(d.values())