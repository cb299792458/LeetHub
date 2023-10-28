class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        vowels = ['a','e','i','o','u']
        next_vowels = {
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a']
        }
        
        curr = 1
        endings = {key: 1 for key in vowels}
        
        for _ in range(n-1):
            new_endings = defaultdict(int)
            for v in vowels:
                for nv in next_vowels[v]:
                    new_endings[nv] += endings[v] % mod
            
            endings = new_endings
            
        return sum(endings.values()) % mod