/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head, history = []) {
    if(!head){return false}
    if(history.includes(head)){return true}
    history.push(head);
    return hasCycle(head.next, history);
};