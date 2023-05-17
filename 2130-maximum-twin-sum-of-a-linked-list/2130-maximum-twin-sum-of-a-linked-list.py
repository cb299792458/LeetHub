# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = deque()
        
        curr = head
        
        while curr:
            nums.append(curr.val)
            curr = curr.next
            
        res = float('-inf')
        while nums:
            res = max(res,nums.pop()+nums.popleft())
        return res