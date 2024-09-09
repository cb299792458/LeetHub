# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        dirs = [
            (0,+1),
            (+1,0),
            (0,-1),
            (-1,0),
        ]
        di = r = c = r_min = c_min = 0
        r_min+=1
        
        curr = head
        while curr:
            # print(r,c)
            res[r][c] = curr.val
            
            if di%4==0 and c==n-1:
                di+=1
                n-=1
            elif di%4==1 and r==m-1:
                di+=1
                m-=1
            elif di%4==2 and c==c_min:
                di+=1
                c_min+=1
            elif di%4==3 and r==r_min:
                di+=1
                r_min+=1
            
            r,c = r+dirs[di%4][0],c+dirs[di%4][1]
            curr = curr.next
        
        return res