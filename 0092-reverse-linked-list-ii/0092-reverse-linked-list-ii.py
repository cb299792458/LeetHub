# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = dummy = ListNode(0,head)
        before = dummy
        after = None
        
        while current.next:
            nextNode = current.next
            left-=1
            right-=1
            
            if left==1:
                before = nextNode
            if right==-1:
                after = nextNode
                current.next = None
            current=nextNode
        
        
        current = before.next
        while current:
            temp = current.next
            
            current.next = after
            after = current
            
            current = temp

        before.next = after
        
        
        return dummy.next