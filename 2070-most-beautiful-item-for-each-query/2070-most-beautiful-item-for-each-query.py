class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        def binary_search(query):
            l, r = 0, len(items)-1
            beauty = 0
            
            while l<=r:
                m = (l+r)//2
                
                if items[m][0]>query:
                    r = m - 1
                else:
                    beauty = items[m][1]
                    l = m + 1
            
            return beauty
            
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        return [binary_search(q) for q in queries]