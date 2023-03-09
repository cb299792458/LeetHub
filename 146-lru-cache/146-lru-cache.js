class Node {
    constructor(key,val,prev,next){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}


class LRUCache {
    constructor(capacity){
        this.capacity = capacity;
        this.hashMap = new Map();
        
        this.head = new Node('head','head');
        this.tail = new Node('tail','tail');
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    delete(node){
        let before = node.prev;
        let after = node.next;
        
        before.next = after;
        after.prev = before;
    }
    
    add(node){
        let second = this.head.next;
        
        this.head.next = node;
        node.prev = this.head;
        
        second.prev = node;
        node.next = second;
    }
    
    
    put(key,val){
        if(this.hashMap.has(key)){
            let node = this.hashMap.get(key);
            this.delete(node);
            this.hashMap.delete(key);
        }
        let node = new Node(key,val);
        this.hashMap.set(key,node);
        this.add(node);
        this.evict();
    }
    
    get(key){
        if(!this.hashMap.has(key)) return -1;
        let node = this.hashMap.get(key);
        this.delete(node);
        this.add(node);
        this.evict();
        return node.val;
    }
    
    evict(){
        if(this.hashMap.size > this.capacity){
            let node = this.tail.prev;
            console.log('deleting ', node.key,node.val);
            this.delete(node);
            this.hashMap.delete(node.key);
        }
    }

}