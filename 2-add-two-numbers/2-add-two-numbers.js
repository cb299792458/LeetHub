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
//     console.log(parseNum(l1),parseNum(l2));
//     const num = parseNum(l1) + parseNum(l2);
    
//     const str = '' + num;
//     const arr = str.split('').reverse();
//     let dummy = new ListNode();
//     let current = dummy;
//     for(let char of arr){
//         current.next = new ListNode(char);
//         current = current.next;
//     }
//     return dummy.next;
    
    let dummy = new ListNode();
    let current = dummy;
    let carry = 0;
    let digit = 0;
    while(l1 || l2 || carry){
        // console.log(l1,l2)
        digit = 0;
        if(l1 && l1.val !== null) digit += l1.val;
        if(l2 && l2.val !== null) digit += l2.val;
        digit += carry;
        // console.log(digit)
        current.next = new ListNode(digit % 10);
        carry = Math.floor(digit/10);
        current = current.next;
        
        if(l1 && l1.val !== null) l1 = l1.next;
        if(l2 && l2.val !== null) l2 = l2.next;
        
        
    }
    return dummy.next;
};

// function parseNum(node){
//     if(!node.next) return node.val
//     return node.val + 10*parseNum(node.next);
// }