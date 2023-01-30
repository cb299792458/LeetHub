/**
 * @param {number} k
 * @param {number[]} nums
 */

class Node{
    constructor(val,next){
        this.val = val;
        this.next = next;
    }
}
var KthLargest = function(k, nums) {
    this.k = k;
    this.head = new Node(Infinity);
    
    for(let num of nums){
        this.add(num);
    }
    
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    let p = this.head;
    let n = p.next
    while(n && n.val>val){
        p = n;
        n = n.next;
    }

    let newNode = new Node(val,n);
    p.next = newNode;

    let current = this.head;
    // while(current){
    //     console.log(current.val);
    //     current = current.next;
    // }
    
    
    
    for(let i=0;i<this.k;i++){
        if(current.next) current = current.next;
//         // console.log(current)
    }
    
    return current.val;
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */