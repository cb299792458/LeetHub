/**
 * @param {number[]} nums
 * @param {number} limit
 * @param {number} goal
 * @return {number}
 */
var minElements = function(nums, limit, goal) {
    let sum=0;
    for(let n of nums) sum+=n;
    return Math.ceil(Math.abs((sum-goal)/limit));
};