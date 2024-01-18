class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = defaultdict(int)
        best = ''
        
        curr = ''
        for char in paragraph+' ':
            if char.isalpha():
                curr += char.lower()
            else:
                if curr and curr not in banned:
                    counts[curr] += 1
                    if counts[curr] > counts[best]:
                        best = curr
                curr = ''
        
        return best