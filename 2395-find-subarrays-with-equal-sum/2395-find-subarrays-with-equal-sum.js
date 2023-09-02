/**
 * @param {number[]} nums
 * @return {boolean}
 */
var findSubarrays = function(nums) {
    const seen = new Set();
    for(let i=0;i<nums.length-1;i++){
        const total = nums[i]+nums[i+1];
        if(seen.has(total)){
            return true;
        } else {
            seen.add(total);
        }
    }
    return false;
};