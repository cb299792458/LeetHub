class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [t[0] for t in sorted(zip(names,heights), key=lambda t: t[1], reverse=True)]