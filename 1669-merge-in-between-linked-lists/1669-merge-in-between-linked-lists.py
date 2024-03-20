# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        end_of_2 = list2
        while end_of_2.next:
            end_of_2 = end_of_2.next
            
        dummy = ListNode(0,list1)
        before_ath = bth = dummy
        for _ in range(a):
            before_ath = before_ath.next
        for _ in range(b+1):
            bth = bth.next
            
        before_ath.next = list2
        end_of_2.next = bth.next
        
        return dummy.next