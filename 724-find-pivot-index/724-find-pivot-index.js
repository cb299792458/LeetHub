/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {

    let length = nums.length;
    let left=0,right=length-1;
    let leftSums = new Array(nums.length);
    let rightSums = new Array(nums.length);
    leftSums[0] = 0;
    rightSums[length-1] = 0;
    
    for(let i=1;i<length;i++){
        leftSums[i] = leftSums[i-1] + nums[i-1];
        rightSums[length-i-1] = rightSums[length-i] + nums[length-i];
    }
    
    // console.log(leftSums,rightSums);
    for(let i=0;i<length;i++) if(leftSums[i]===rightSums[i]) return i
    return -1;
};