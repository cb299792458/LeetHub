var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0,head);
    let slow = dummy;
    let fast = head;
    
    while(n > 0){
        fast = fast.next;
        n--;
    }
    while(fast){
        fast = fast.next;        
        slow = slow.next;   
    }
    
    slow.next = slow.next.next;
    
    return dummy.next;
};