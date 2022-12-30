/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    nums = nums.sort((a,b) => {return a-b});
    console.log(nums)
    for(let i = nums.length - 1; i > 1; i--){
        if(nums[i] < nums[i-1] + nums[i-2]) return nums[i] + nums[i-1] + nums[i-2]
    }
    return 0
};