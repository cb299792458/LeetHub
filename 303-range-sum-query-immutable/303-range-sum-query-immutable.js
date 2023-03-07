/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.array = nums;
    this.sums = new Array(nums.length);
    let sum = 0;
    for(let i=0;i<nums.length;i++){
        sum+=nums[i];
        this.sums[i] = sum;
    }
};
/*
[-2, 0,3,-5, 2,-1]
[-2,-2,1,-4,-2,-3]
     ^-L     R
*/


/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    // let sum = 0;
    // for(let i = left;i<=right;i++){
    //     sum += this.array[i];
    // }
    // return sum;
    return this.sums[right] - (left ? this.sums[left-1] : 0);
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */