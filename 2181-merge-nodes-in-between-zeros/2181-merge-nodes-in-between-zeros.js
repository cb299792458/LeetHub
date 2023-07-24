var mergeNodes = function(head) {
    let current = head;
    let dummy = new ListNode();
    
    let resultTail = dummy;
    
    while(current.next){
        if(current.val===0){
            // 0 >> make new node for result
            resultTail.next = new ListNode(0);
            resultTail = resultTail.next;
        } else {
            // non-zero .. add current.val to newest node in result
            resultTail.val += current.val;
        }
        current=current.next;
    }
    
    return dummy.next;
};