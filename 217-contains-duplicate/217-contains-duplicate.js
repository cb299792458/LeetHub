/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let contained = [];
    let ans = false;
    nums.forEach((num)=>{
        if(contained.includes(num)){
            ans = true;
        }
        contained.push(num);
    });
    return ans;
};