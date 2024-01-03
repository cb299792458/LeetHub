class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        prev = bank[0].count('1')
        for line in bank[1:]:
            curr = line.count('1')
            if curr:
                lasers += prev*curr
                prev = curr
        return lasers