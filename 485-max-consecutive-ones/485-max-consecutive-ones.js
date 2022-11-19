/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let ones = 0;
    let current = 0;
    nums.forEach((num)=>{
        if(num===1){
            current++;
        } else {
            current = 0;
        }
        if(current>ones){
            ones = current;
        }
    })
    return ones;
};