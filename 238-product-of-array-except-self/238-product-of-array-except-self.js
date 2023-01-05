/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let left = new Array(nums.length);
    let right = new Array(nums.length);
    let res = new Array(nums.length);
    let prodLeft = 1;
    let prodRight = 1;
    
    for(let i=0;i<nums.length;i++){
        left[i] = prodLeft;
        right[nums.length-1-i] = prodRight;
        prodLeft *= nums[i];
        prodRight *= nums[nums.length-1-i];
    }
    
    for(let i=0;i<nums.length;i++){
        res[i] = left[i]*right[i];
    }
    
    return res;
};