# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_prev = low_dummy = ListNode(0,head)
        high_prev = high_dummy = ListNode()
        current = head
        
        while current:
            if current.val<x:
                low_prev = current
                current = current.next
            else:
                low_prev.next = current.next
                
                high_prev.next = current
                high_prev = current
                
                current = current.next
                
        high_prev.next = None
        low_prev.next = high_dummy.next
        
        current=low_dummy.next
        # while current:
        #     print(current.val)
        #     current=current.next
        return low_dummy.next