class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = Counter()
        best = ('', 0) # word, frequency
        banned = set(banned)
        
        curr = ''
        for char in list(paragraph+' '):
            if not char.isalpha():
                if curr and curr not in banned:
                    counts[curr] += 1
                    if counts[curr] > best[1]:
                        best = (curr, counts[curr])
                curr=''
            else:
                curr += char.lower()
        
        return best[0]