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
    let head = new ListNode();
    
    let current = head;
    while(current){
        let next = null;
        for(let i=0;i<lists.length;i++){
            if(!lists[i]) continue;
            if(lists[next]===undefined || lists[next].val > lists[i].val) next = i;
        }
        if(lists[next]) {
            current.next = new ListNode(lists[next].val);

            lists[next] = lists[next].next;
        }
        current = current.next;

        
    }
    
    return head.next;
};