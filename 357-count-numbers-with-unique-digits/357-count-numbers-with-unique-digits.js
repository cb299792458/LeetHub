/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    let dp = [1]
    
    for(let i=1;i<=n;i++){
        let thisRow = 9; // 9 choices for first digit
        let multiplier = 9; // 10-1 choices for next digit
        for(let digit = i; digit > 1 ; digit--){ // every following digit has one less choice
            thisRow *= multiplier;
            multiplier--;
        }
        
        dp[i] = thisRow + dp[i-1];
    }
    
    return dp[n];
};