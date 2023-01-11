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
var middleNode = function(head) {
    // let arr = [];
    // while(head){
    //     arr.push(head);
    //     head = head.next;
    // }
    // // console.log(arr);
    // return arr[Math.floor((arr.length)/2)];
    let slow = head;
    let fast = head;
    while(fast && fast.next){
        fast = fast.next.next;
        
        slow = slow.next;
    }
    return slow;
};