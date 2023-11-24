class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        dq = deque(piles)
        coins = 0
        while dq:
            dq.pop()
            coins+=dq.pop()
            dq.popleft()
        return coins