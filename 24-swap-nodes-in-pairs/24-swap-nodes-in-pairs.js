/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    let dummy = new ListNode(0,head);
    let current = dummy;
    while(current.next && current.next.next){
        let a = current.next;
        let b = a.next;
        
        a.next = b.next;
        b.next = a;
        current.next = b;
        current = a;
    }
    return dummy.next;
};