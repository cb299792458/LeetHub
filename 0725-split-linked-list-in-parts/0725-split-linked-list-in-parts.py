# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        length, remainder = length // k, length % k

        parts=[]
        curr=head
        
        while curr:
            parts.append(curr)
            part_len = length
            if remainder:
                part_len+=1
                remainder-=1
            
            while part_len and curr:
                part_len-=1
                prev=curr
                curr=curr.next
            prev.next = None
        
        while len(parts)<k:
            parts.append(None)
        return parts
            