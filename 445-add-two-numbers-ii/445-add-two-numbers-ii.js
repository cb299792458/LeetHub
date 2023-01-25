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
    const stack1 = [];
    const stack2 = [];
    
    while(l1){
        stack1.push(l1.val);
        l1 = l1.next;
    }
    while(l2){
        stack2.push(l2.val);
        l2 = l2.next;
    }
    
    let carry = 0;
    let curr = null;
    while(stack1.length || stack2.length || carry){
        let prev = curr;
        
        const dig1 = stack1.pop();
        const dig2 = stack2.pop();
        if(dig1) carry += dig1;
        if(dig2) carry += dig2;
        
        curr = new ListNode(carry%10,prev);
        carry = Math.floor(carry/10);
    }
    
    return curr;
};