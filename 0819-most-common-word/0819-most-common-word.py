class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for s in symbols:
            paragraph = paragraph.replace(s, ' ')
        paragraph = paragraph.lower()
            
        counts = Counter()
        best = ('', 0)
        for word in paragraph.split():
            if word not in banned:
                counts[word] += 1
                if counts[word] > best[1]:
                        best = (word, counts[word])
        return best[0]