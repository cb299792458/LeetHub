/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let left = 0, right = 0;
    
    for(;right<nums.length;){
        if(nums[right]===val){
            right++;
        } else {
            nums[left] = nums[right];
            left++;
            right++;
        }
    }
    return left;
};