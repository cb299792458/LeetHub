/**
 * @param {number} capacity
 */
class Node{
    constructor(key,val,next,prev){
        this.key = key;
        this.val = val;
        this.next = next;
        this.prev = prev;
    }
}

var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.map = new Map;
    this.head = new Node();
    this.tail = new Node();
    this.head.next = this.tail;
    this.tail.prev = this.head;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if(!this.map.has(key)) return -1;
    
    let node = this.map.get(key);
    
    let before = node.prev;
    let after = node.next;
    before.next = after;
    after.prev = before
    
    let second = this.head.next;
    this.head.next = node;
    node.prev = this.head;
    node.next = second;
    second.prev = node;

    return node.val
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    let node;
    if(!this.map.has(key)){
        node = new Node(key, value);
        this.map.set(key,node);
    } else {
        node = this.map.get(key);
        node.val = value;
        this.map.set(key,node);
        
        let before = node.prev;
        let after = node.next;
        before.next = after;
        after.prev = before
    }
    
    let second = this.head.next;
    this.head.next = node;
    node.prev = this.head;
    node.next = second;
    second.prev = node;
    
    if(this.map.size > this.capacity){
        let last = this.tail.prev;
        let nextToLast = last.prev;
        
        nextToLast.next = this.tail;
        this.tail.prev = nextToLast;
        this.map.delete(last.key);
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */