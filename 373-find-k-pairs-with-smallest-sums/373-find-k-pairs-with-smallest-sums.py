class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap=[]
        seen=set()
        
        def my_heap_push(i,j):
            if i==len(nums1) or j==len(nums2): return
            tup = (nums1[i]+nums2[j],i,j)
            if tup in seen: return
            seen.add(tup)
            
            heappush(min_heap,tup)
            
        my_heap_push(0,0)
        
        res=[]
        while min_heap and len(res)<k:
            (_,i,j) = heappop(min_heap)
            res.append([nums1[i],nums2[j]])
            my_heap_push(i+1,j)
            my_heap_push(i,j+1)
        return res