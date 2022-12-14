/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let left = 0;
    let right = 0;
    let length = Infinity;
    let sum = 0;
    while(left <= nums.length){
        if(sum<target && right<nums.length){
            sum += nums[right];
            right++;
        } else {
            sum -= nums[left];
            left++;
        }
        if(sum >= target){
            length = Math.min(length, right - left);
        }
    }
    return length === Infinity ? 0 : length;
};