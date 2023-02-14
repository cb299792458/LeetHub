/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head, seen = new Set()) {
    if(!head) return null;
    if(seen.has(head)) return head;
    seen.add(head);
    
    return detectCycle(head.next,seen);
};