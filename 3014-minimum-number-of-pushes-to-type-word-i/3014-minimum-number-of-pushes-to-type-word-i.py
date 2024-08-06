class Solution:
    def minimumPushes(self, word: str) -> int:
        N = len(word)
        pushes = 0
        for i in range(N):
            pushes += 1 + i//8
        return pushes