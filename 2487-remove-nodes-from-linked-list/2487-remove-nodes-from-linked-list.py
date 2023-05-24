# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        stack = []
        
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            
            stack.append(curr)
            curr = curr.next
            
        curr = dummy
        for node in stack:
            curr.next = node
            curr = node
            
        return dummy.next