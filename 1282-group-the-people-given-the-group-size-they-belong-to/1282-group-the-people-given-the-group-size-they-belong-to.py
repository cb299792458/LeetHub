class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        
        for (i,n) in enumerate(groupSizes):
            if not groups[n] or len(groups[n][-1])==n:
                groups[n].append([i])
            else:
                groups[n][-1].append(i)
        
        res = []
        for subgroups in groups.values():
            for group in subgroups:
                res.append(group)
        return res