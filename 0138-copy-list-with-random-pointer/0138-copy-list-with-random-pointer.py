"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = dummy = Node(0)
        orig = head
        copies = dict()
        
        while orig:
            copies[orig] = Node(orig.val)
            curr.next = copies[orig]
            curr = curr.next
            orig = orig.next
            
        orig = head
        curr = dummy.next
        while orig:
            curr.random = copies[orig.random] if orig.random in copies else None
            curr = curr.next
            orig = orig.next
        
        return dummy.next