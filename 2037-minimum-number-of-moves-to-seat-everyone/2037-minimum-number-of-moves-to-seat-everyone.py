class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for [a,b] in zip(seats,students):
            moves += abs(a-b)
        return moves