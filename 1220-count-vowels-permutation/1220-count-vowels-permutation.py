class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        vowels = 'aeiou'
        next_vowels = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a'
        }
        
        curr = 1
        endings = {key: 1 for key in vowels}
        
        while curr<n:
            new = defaultdict(int)
            for v in vowels:
                for nv in next_vowels[v]:
                    new[nv] += endings[v]
            
            endings = new
            curr+=1
            
        return sum(endings.values()) % mod