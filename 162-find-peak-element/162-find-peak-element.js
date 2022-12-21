/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    if(nums.length === 1) return 0;
    let left = 0;
    let right = nums.length - 1;
    
    while(left <= right){
        const mid = Math.floor((left+right)/2);
        console.log(left,right,mid)
        if((nums[mid-1]===undefined || nums[mid]>nums[mid-1])&&(nums[mid+1]===undefined || nums[mid]>nums[mid+1])) return mid;
        if(nums[mid]<nums[mid+1]){
            left = mid+1;
        } else {
            right = mid-1;
        }
    }
    
};