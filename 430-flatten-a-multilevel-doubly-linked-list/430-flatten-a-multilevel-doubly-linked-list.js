/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var flatten = function(head, beforeHead=null, afterTail=null) {
    if(!head) return null;
    
    
    head.prev = beforeHead;
    if(beforeHead) beforeHead.next = head;
    
    let current = head;
    
        if(current.child){ //2 
        let currentTail = current.next; //null
            
        current.next = flatten(current.child, current, currentTail); //2,1,null
        current.child = null;
    } 
    
    while(current.next){ //3  //8 //12
        if(current.child){ //7   //11
            let currentTail = current.next; //4 //9
            
            current.next = flatten(current.child, current, currentTail); //(7,3,4)  //11,8,9
            current.child = null;
            
            
        } else {
            current = current.next;
        }
    }
    
    

    
    if(current) current.next = afterTail;
    if(afterTail) afterTail.prev = current;
    
    return head;
};