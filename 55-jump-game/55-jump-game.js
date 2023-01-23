/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let maxReach = 0;
    let i = 0;
    while(i<=maxReach && i < nums.length){
        maxReach = Math.max(maxReach,nums[i]+i);
        if(maxReach >= nums.length - 1) return true
        i++;
    }
    return false
    


};