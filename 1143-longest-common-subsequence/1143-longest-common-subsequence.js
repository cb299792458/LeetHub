/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    
    let dp = new Array(text1.length);
    for(let i = 0; i <= text1.length; i++){
        dp[i] = new Array(text2.length+1);
    }
    
    for(let j=0;j<dp.length;j++){
        dp[j][0]=0;
    }
    
    for(let k=0;k<dp[0].length;k++){
        dp[0][k]=0;
    }
    
    for (let row = 1; row < dp.length; row++) {
        for (let col = 1; col < dp[0].length; col++) {
            if(text1[row-1] === text2[col-1]){
                // console.log(row,col)
                dp[row][col] = dp[row-1][col-1] + 1;
            } else {
                dp[row][col] = Math.max( dp[row-1][col], dp[row][col-1] );
            }
        }
    };
    
    // console.log(dp);
    return dp.at(-1).at(-1);
};