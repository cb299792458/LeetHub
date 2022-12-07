/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const set = new Set(nums);
    // console.log(set.entries());
    return set.size !== nums.length;
};