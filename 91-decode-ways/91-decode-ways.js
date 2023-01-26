/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if(s[0]==='0' || s.length===0) return 0;
    const dp = [1];
    for(let i=1;i<s.length;i++){
        dp[i] = 0;
        const one = parseInt(s.slice(i,i+1));
        const two = parseInt(s.slice(i-1,i+1));
        if(one > 0){
            dp[i] += dp[i-1];
        }
        if(two<27 && two>9){
            dp[i] += dp[i-2]!==undefined ? dp[i-2] : 1;
        }
        if(two==0) return 0;
        

    }
    console.log(dp)
    return dp.at(-1);
};