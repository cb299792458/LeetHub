# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_int(l):
            if not l.next:
                return l.val
            
            return l.val + 10 * linked_list_to_int(l.next)
        
        sum_of_lists = linked_list_to_int(l1) + linked_list_to_int(l2)
        # 80
        
        dummy = ListNode(0, None)
        curr = dummy
        
        if sum_of_lists == 0:
            return ListNode(0)
        
        while sum_of_lists:
            digit = sum_of_lists % 10
            curr.next = ListNode(digit, None)
            
            curr = curr.next
            sum_of_lists = sum_of_lists // 10
        
        return dummy.next
            