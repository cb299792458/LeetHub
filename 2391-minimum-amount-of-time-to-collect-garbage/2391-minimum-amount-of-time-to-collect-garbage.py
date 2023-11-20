class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = sum([len(s) for s in garbage])
        types = ['M', 'P', 'G']
        last_index = {t: 0 for t in types}

        for i,g in enumerate(garbage):
            for t in types:
                if t in g:
                    last_index[t] = i
                    
        travel = [0] + travel
        # print(time, travel, last_index)
        for t in types:
            time += sum(travel[:last_index[t]+1])
        return time