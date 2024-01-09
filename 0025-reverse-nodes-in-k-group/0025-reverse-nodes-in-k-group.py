# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        dummy = ListNode(0,head)
        groups = length // k
        start = dummy
        
        for _ in range(groups):
            to_reverse = []
            curr = start.next
            for _ in range(k):
                to_reverse.append(curr)
                curr = curr.next
            
            for node in to_reverse:
                node.next = curr
                curr = node
                
            start.next = to_reverse[-1]
            start = to_reverse[0]
        
        return dummy.next
            