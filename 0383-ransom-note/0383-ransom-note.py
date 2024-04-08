class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        needed = Counter(ransomNote)
        available = Counter(magazine)
        
        for char, count in needed.items():
            if count > available[char]:
                return False
        return True