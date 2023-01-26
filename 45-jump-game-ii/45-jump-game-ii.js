/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    const n = nums.length;
    const memo = [0];
    
    for(let i=0;i<n;i++){
        for(let jumps = nums[i]; jumps > 0; jumps--){
            if(!memo[i+jumps]){
                memo[i+jumps] = memo[i]+1;
            }
            
        }
    }
    return memo[n-1]
};