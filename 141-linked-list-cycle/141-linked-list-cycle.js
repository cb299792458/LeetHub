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
    if(history.includes(head)){return true}
    history.push(head);
    if(!head){return false}
    return hasCycle(head.next, history);

       
};