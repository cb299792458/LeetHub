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
    if(!node.next) return;
    temp = node.next;
    
    node.val = temp.val;
    node.next = temp.next;
    
    // deleteNode(temp);
    
    
//     let curr = node;
    
//     while(curr){
//         console.log('handling node #', curr.val)
//         let temp = curr.next;
        
//         if(curr.next){
//             curr.val = temp.val;
//             curr.next = temp.next;
//         }
        
//         curr = temp;
//     }
};