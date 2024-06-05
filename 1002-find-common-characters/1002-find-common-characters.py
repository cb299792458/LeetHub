class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words[1:]:
            curr = Counter(word)
            for [char, count] in counts.items():
                counts[char] = min(count, curr[char])
        
        all_chars = []
        for [char, count] in counts.items():
            for _ in range(count):
                all_chars.append(char)
        
        return all_chars