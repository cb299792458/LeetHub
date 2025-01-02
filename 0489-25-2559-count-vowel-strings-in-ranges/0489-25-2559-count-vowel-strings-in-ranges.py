class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        valids = [word[0] in vowels and word[-1] in vowels for word in words]

        prefix_sum = [0]
        count = 0
        for word in valids:
            count += int(word)
            prefix_sum.append(count)
        
        res = []
        for [s,e] in queries:
            res.append(prefix_sum[e+1]-prefix_sum[s])
        return res