/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    const colors = [0,1,2];
    const res = [];
    for(let color of colors){
        for(let num of nums){
            if(num===color) res.push(num);
        }
    }

    for(let i in res){
        nums[i] = res[i];
    }
};