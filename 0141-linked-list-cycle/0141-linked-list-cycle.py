# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
myDict = {myKey: myValue}
myObject.myKey = myValue

head = {
    val: 1,
    next: {
        val: 2,
        next: None
    }
}
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        
        curr = head
        while curr != None:
            if curr in seen:
                return True
            seen.append(curr)
            curr = curr.next
        return False