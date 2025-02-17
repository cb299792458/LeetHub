class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counts):
            res = 0

            for [char, count] in counts.items():
                if not count:
                    continue
                res += 1

                counts[char] -= 1
                res += backtrack(counts)
                counts[char] += 1

            return res
        
        return backtrack(Counter(tiles))