/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if(nums.length === 0){
        return -1;
    }
    const mi = Math.floor(nums.length/2);
    if(nums[mi]===target){return mi}
    if(nums[mi]>target){
        const ans = search(nums.slice(0,mi),target);
        return ans === -1 ? -1 : ans;
    } else {
        const ans = search(nums.slice(mi+1,nums.length),target);
        return ans === -1 ? -1 : mi + ans + 1;
    }
}