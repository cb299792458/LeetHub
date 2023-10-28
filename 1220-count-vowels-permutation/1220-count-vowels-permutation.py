class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        vowels = 'aeiou'
        nexts = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a'
        }
        
        curr = 1
        ends = {key: 1 for key in vowels}
        
        while curr<n:
            new = defaultdict(int)
            for v in vowels:
                for nx in nexts[v]:
                    new[nx] += ends[v]
            
            ends = new
            curr+=1
            
        return sum(ends.values()) % mod