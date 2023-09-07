var reverseList = function(head) {
//     if(!head || !head.next) return head;
    
//     let end = reverseList(head.next);
    
//     head.next.next = head;
//     head.next = null
    
//     return end;
    
    let prev = null
    
    while(head){
        let oldNext = head.next;
        head.next = prev;
        
        prev = head;
        head = oldNext;
    }
    
    return prev;
};