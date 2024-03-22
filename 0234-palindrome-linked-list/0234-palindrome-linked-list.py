class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        current=head
        while current:
            vals.append(current.val)
            current=current.next
        copy = vals.copy()
        vals.reverse()
        return copy==vals