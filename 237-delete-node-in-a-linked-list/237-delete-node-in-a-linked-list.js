/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    temp = node.next;
    
    node.val = node.next.val;
    node.next = node.next.next;
    
};

/*

[4,5,9]
 4,1,9,X
 4,1,9
 
 
 
5

*/