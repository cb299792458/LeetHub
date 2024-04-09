class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i]:
                    tickets[i] -= 1
                    time += 1
                if i==k:
                    if not tickets[i]:
                        return time