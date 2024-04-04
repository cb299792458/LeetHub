class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def adj(beg, end):
            diffs = 0
            for c1, c2 in zip(beg,end):
                if c1!=c2:
                    diffs+=1
            return diffs<2
        
        steps = dict()
        steps[beginWord] = 1
        
        queue = deque([beginWord])
        
        while queue:
            curr = queue.popleft()
            for neighbor in wordList:
                if neighbor in steps:
                    continue
                if not adj(curr,neighbor):
                    continue
                
                steps[neighbor] = steps[curr] + 1
                queue.append(neighbor)
            if endWord in steps: break

        return steps[endWord] if endWord in steps else 0