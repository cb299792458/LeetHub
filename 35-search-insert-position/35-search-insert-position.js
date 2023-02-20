/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left=0,right=nums.length-1;
    
    while(left<right){
        let mid = Math.floor((left+right)/2);
        if(nums[mid]===target) return mid;
        if(nums[mid]<target){
            left = mid+1;
        } else {
            right = mid;
        }
    }
    console.log(left)
    // if(nums[left]===target) return left;
    if(nums[left]<target) return left+1;
    // if(nums[left]>target) return left-1;
    return left;
};