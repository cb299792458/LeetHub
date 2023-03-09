/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    
    while(left<=right){
        let mid = Math.floor((left+right)/2);
        if(nums[mid]===target) return true;
        console.log(left,mid,right)
        if (nums[mid] == nums[right]){
            right--;
            continue;
        }
        
        if(nums[left]<=nums[mid]){
            if(nums[left]<=target && target<=nums[mid]){
                right = mid-1;
            } else {
                left = mid+1;
            }
        } else {
            if(target>=nums[mid] && target<=nums[right]){
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
    }
    
    return false;
};