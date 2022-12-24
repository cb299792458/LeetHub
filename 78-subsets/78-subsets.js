/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if(!nums.length) return [[]];
    
    const results = [];
    const first = nums.shift();
    const nextSets = subsets(nums);
    console.log(nextSets)
    for(let i=0;i<nextSets.length;i++){
        const nextSet = nextSets[i];
        results.push(nextSet);
        results.push(nextSet.concat(first));
    }
    return results;
};