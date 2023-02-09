/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    
    let dummy = new ListNode();
    let current = dummy;
    let carry = 0;
    let digit = 0;
    while(l1 || l2 || carry){
        digit = 0;
        if(l1) digit += l1.val;
        if(l2) digit += l2.val;
        digit += carry;

        current.next = new ListNode(digit % 10);
        carry = Math.floor(digit/10);
        current = current.next;
        
        if(l1) l1 = l1.next;
        if(l2) l2 = l2.next;
        
    }
    return dummy.next;
};

