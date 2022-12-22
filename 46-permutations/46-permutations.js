/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    if(nums.length<2) return [nums];
    const first = nums.shift();
    const res = [];
    const prev = permute(nums);
    for(let i = 0; i < prev.length; i++){
        for(let j = 0; j <= prev[i].length; j++){
            res.push( prev[i].slice(0,j).concat(first).concat(prev[i].slice(j)) )
        }
    }
    return res;
};