/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    let sum = 0;
    let val = 0;
    for (let i=0;i<nums.length;i++) {
        val += i * nums[i];
        sum += nums[i];
    }
    let best = val;
    
    for (let j=nums.length-1;j>0;j--) {
        val += sum;
        val -= nums.length * nums[j];
        best = Math.max(best, val)
    }
    
    return best
    
};