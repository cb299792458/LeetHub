# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
myDict = {myKey: myValue}

head = {
    val: 3,
    next: {
        val: 2,
        next: {
            val: 0,
            next: {
                val: -4,
                next: None
            }
        }
    }
}
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        curr = head
        
        while curr:
            if curr in seen:
                return True
            seen.append(curr)
            curr = curr.next
        
        return False