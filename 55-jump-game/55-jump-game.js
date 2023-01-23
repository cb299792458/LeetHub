/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
//     let dp = new Array(nums.length).fill(false);
//     dp[0] = true;
    
//     for(let i=0;i<nums.length;i++){
//         if(dp[i]){
//             for(let j=1;j<=nums[i];j++){
//                 if(!dp[i+j]) dp[i+j] = true;
//             }
//         }
//     }
    
//     return dp.at(-1);
    
    let maxReach = 0;
    let i = 0;
    while(i<=maxReach && i < nums.length){
        maxReach = Math.max(maxReach,nums[i]+i);
        i++;
    }
    return maxReach >= (nums.length - 1)
};