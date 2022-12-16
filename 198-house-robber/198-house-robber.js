/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length<2){return nums[0]}
    let max = [nums[0],Math.max(nums[0],nums[1])];
    for(let i = 2; i < nums.length; i++){
        max[i] = Math.max(max[i-2] + nums[i], max[i-1]);
    }
    console.log(max);
    return Math.max(max.at(-1),max.at(-2));
    
};