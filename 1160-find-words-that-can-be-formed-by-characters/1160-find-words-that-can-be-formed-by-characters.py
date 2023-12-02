class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        lengths = 0
        
        for word in words:
            counts = Counter(word)
            can_make = True
            for c in word:
                # print(c, counts[c], chars[c])
                if counts[c]>chars[c]:
                    can_make = False
                    break
            
            if can_make:
                # print(word)
                lengths += len(word)
        
        return lengths