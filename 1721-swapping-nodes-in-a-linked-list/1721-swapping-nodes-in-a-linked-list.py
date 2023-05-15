# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for _ in range(1,k):
            fast = fast.next
            
        first = fast
        fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
            
        second = slow
        
        first.val, second.val = second.val, first.val
        
        return head