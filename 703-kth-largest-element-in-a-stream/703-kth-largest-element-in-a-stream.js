/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.elements = [...nums].sort((a,b)=>{return a-b});
    this.k = k;
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    this.elements.push(val);
    this.elements = this.elements.sort((a,b)=>{return a-b});
    let index = this.elements.length > 2 ? -3 : -1;
    console.log(this.elements)
    return this.elements.at(-this.k)
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */