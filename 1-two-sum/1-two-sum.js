/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let obj = {};
    let ans = [];
    nums.forEach((num,i)=>{
        if(obj[target-num] || obj[target-num] === 0){
            ans = [obj[target-num],i]
        }
        obj[num] = i;
    });
    return ans;
    

};