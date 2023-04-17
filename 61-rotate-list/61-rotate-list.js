/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    let fast = head;
    let slow = head;
    const oldHead = head;
    
    k = k % findLength(head)
    if(!head) return null;
    if(!head.next || !k) return head;

    
    for(let i=0;i<k;i++){
        fast = fast.next;
    }
    
    while(fast.next){
        fast = fast.next;
        slow = slow.next;
    }

    const newHead = slow.next;
    fast.next = oldHead;
    slow.next = null;
    return newHead;
};
function findLength(head){
    let count = 0;
    let current = head;
    while(current){
        count++;
        current = current.next;
    }
    return count;
}