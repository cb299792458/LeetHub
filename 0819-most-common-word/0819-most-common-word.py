class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = Counter()
        symbols = set(list(' !?\',;.'))
        banned = set(banned)
        
        curr = ''
        for char in list(paragraph+' '):
            if not char.isalpha():
                if curr and curr not in banned:
                    counts[curr] += 1
                curr=''
            else:
                curr += char.lower()
        
        words_and_freqs = [(freq, word) for [word, freq] in counts.items()]
        words_and_freqs.sort(reverse=True)
        return words_and_freqs[0][1]