# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crits = []
        idx = 1
        
        curr = head
        while curr and curr.next and curr.next.next:
            if curr.next.val > curr.val and curr.next.val > curr.next.next.val:
                crits.append(idx)
            if curr.next.val < curr.val and curr.next.val < curr.next.next.val:
                crits.append(idx)
            curr = curr.next
            idx += 1
            
        if len(crits) < 2:
            return [-1,-1]
        
        return [
            min([crits[i+1]-crits[i] for i in range(len(crits)-1)]),
            crits[-1]-crits[0]
        ]