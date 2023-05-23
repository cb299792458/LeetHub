/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    
    while(left<=right){
        let mid = Math.floor((left+right)/2);
        if(nums[mid]===target) return mid;
        
        if(nums[left] <= nums[mid]){
            // left not rotated
            if(nums[left]<=target && target<nums[mid]){
                right = mid;
            } else {
                left = mid + 1;
            }
        } else {
            // right not rotated
            if(nums[mid]<target && target<=nums[right]){
                left = mid + 1;
            } else {
                right = mid;
            }
        }
    }
    // if(nums[left]===target) return left;
    return -1;
};