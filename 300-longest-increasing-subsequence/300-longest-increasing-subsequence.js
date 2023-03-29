var lengthOfLIS = function(nums) {

    let dp = new Array(nums.length).fill(1);
    let max = 1;
    
    for(let i=0;i<nums.length;i++){
        for(let j=i+1;j<nums.length;j++){
            if(nums[i]<nums[j]) dp[j] = Math.max(dp[i]+1,dp[j]);
            max = Math.max(max,dp[j]);
        }
    }
    
    return max;
};