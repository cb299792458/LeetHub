# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        current = dummy
        
        while current.next and current.next.next:
            a = current.next
            b = current.next.next
            
            a.next = b.next
            b.next = a
            
            current.next = b
            current = a
            
        return dummy.next