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
    // if(!node.next) return;
    temp = node.next;
    
    node.val = temp.val;
    node.next = temp.next;
    
};

/*

[4,5,9]
 4,1,9,X
 4,1,9
 
 
 
5

*/