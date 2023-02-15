/**
 * @param {number} k
 * @param {number[]} nums
 */
class KthLargest{
    constructor(k, nums) {
        this.k = k
        this.mpq = new MinPriorityQueue();
        for(let num of nums) this.mpq.enqueue(num);
        
                while(this.mpq.size() > this.k) this.mpq.dequeue();

    };

/** 
 * @param {number} val
 * @return {number}
 */
    add(val) {
        this.mpq.enqueue(val);

        if(this.mpq.size() > this.k) this.mpq.dequeue();

        return this.mpq.front().element
    };
}
/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */