class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        for i, sandwich in enumerate(sandwiches):
            if not counts[sandwich]:
                return len(sandwiches)-i
            else:
                counts[sandwich] -= 1
        return 0