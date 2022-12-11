/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let left = 0;
    let right = 1;
    let sum = nums[0];
    let max = sum;
    while(right < nums.length){
        let prefix = sum;
        sum += nums[right];
        if(prefix < 0){
            left = right;
            sum -= prefix;
        }
        
        max = Math.max(max, sum);
        right++;
    }
    return max;
};