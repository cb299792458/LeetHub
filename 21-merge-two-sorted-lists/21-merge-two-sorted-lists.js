/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // // RECURSIVE node by node
    // if(!list1){return list2}
    // if(!list2){return list1}
    // if(list1.val <= list2.val){
    //     list1.next = mergeTwoLists(list1.next, list2);
    //     return list1;
    // } else {
    //     list2.next = mergeTwoLists(list1, list2.next);
    //     return list2;
    // }
    
    // ITERATIVE same as mergesort
    if(!list1) return list2
    if(!list2) return list1
    
    const dummy = new ListNode()
    let current = dummy;

    while(list1 && list2){
        if(list1.val<list2.val){
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    
    current.next = list1 || list2;
    return dummy.next;
};