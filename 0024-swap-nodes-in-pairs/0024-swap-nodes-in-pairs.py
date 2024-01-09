# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        w = dummy
        
        while w.next and w.next.next:
            # d 1 2 3 
            # w x y z
            x = w.next
            y = x.next
            z = y.next

            # swap
            w.next = y
            y.next = x
            x.next = z
        
            w = w.next.next

        return dummy.next