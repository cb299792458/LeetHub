class Solution:
    def compressedString(self, word: str) -> str:
        chars = []
        count = 0
        prev = ''
        
        for char in word:
            if prev==char and count < 9:
                count += 1
            else:
                if count:
                    chars.append(str(count))
                    chars.append(prev)
                prev = char
                count = 1
        
        chars.append(str(count))
        chars.append(prev)
        
        return ''.join(chars)