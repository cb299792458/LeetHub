/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if(n<1) return 1;
    
    // answers with n digits
    let ans = 9; // 9 choices for first digit
    let multiplier = 9; // 10-1 choices for next digit
    for(let digit = n; digit > 1 ; digit--){ // every following digit has one less choice
        ans *= multiplier;
        multiplier--;
    }
    
    // answers with n-1 digits
    ans += countNumbersWithUniqueDigits(n-1);
    
    return ans;
};