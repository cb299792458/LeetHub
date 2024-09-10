# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next = head.next
        
        while next:
            curr.next = ListNode(math.gcd(curr.val,next.val),next)
            curr=next
            next=next.next
        
        return head