class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = defaultdict(list)
        for i,c in enumerate(s):
            indices[c].append(i)
            
        subs = 0
        for index_list in indices.values():
            if len(index_list)>1:
                l,r = index_list[0], index_list[-1]
                subs += len(set(list(s[l+1:r])))
        return subs