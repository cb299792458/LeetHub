class SeatManager:

    def __init__(self, n: int):
        self.reserved=[i for i in range(1,n+1)]
        heapq.heapify(self.reserved)

    def reserve(self) -> int:
        return heapq.heappop(self.reserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.reserved,seatNumber)