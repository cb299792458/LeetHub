/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if(!lists.length) return null;
    for(let i=1;i<lists.length;i++){
        lists[0] = mergeTwoLists(lists[0],lists[i]);
    }
    return lists[0];
};

function mergeTwoLists(l1,l2){
    let head = new ListNode();
    let curr = head;
    while(l1 && l2){
        if(l1.val>l2.val){
            curr.next = l2;
            l2 = l2.next;
        } else {
            curr.next = l1;
            l1 = l1.next;
        }
        curr = curr.next;
    }
    if(l1) curr.next = l1;
    if(l2) curr.next = l2;
    return head.next;
}