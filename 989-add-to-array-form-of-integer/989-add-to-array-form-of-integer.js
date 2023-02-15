/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let numIdx = num.length-1;
    let ans = [];
    
    let carry = 0;
    while(k || carry || numIdx >= 0){
        let digit = k % 10;
        let numDigit = (num[numIdx] ? num[numIdx] : 0)
        
        let sum = carry + digit + numDigit;
        
        ans.push(sum%10);
        carry = Math.floor(sum/10);
        k = Math.floor(k/10);
        numIdx--;
    }

    return ans.reverse();
};