/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {

    let sum = 0;
    
    for(let num of nums){
        sum+=num;
    }
    
    let leftSum = 0;
    for(let i=0;i<nums.length;i++){
        if((sum-nums[i])/2 === leftSum) return i;
        leftSum += nums[i];
    }
    return -1
};