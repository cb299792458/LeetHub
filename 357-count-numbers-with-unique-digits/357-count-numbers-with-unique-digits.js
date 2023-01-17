/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if(n<1) return 1;
    
    // answers with n digits
    let ans = 9;
    let multiplier = 9;
    for(let digit = n; digit > 1 ; digit--){
        ans *= multiplier;
        multiplier--;
    }
    
    // answers with n-1 digits
    ans += countNumbersWithUniqueDigits(n-1);
    
    return ans;
// 2 9x9
// 3 9x9x8
// 4 9x9x8x7
// 5 9x9x8x7x6
    
//     return ans - something;
    
    //BRUTE FORCE
//     let nums = [];
//     for(let i=0;i<10**n;i++){ // 12344
//         let str = '' + i;
        
//         let match = false;
        
//         for(let j=0;j<str.length;j++){ // '0'
//             for(k=j+1;k<str.length;k++){
//                 if(str[j]===str[k]) match = true;
//             }
//         }
        
//         if(!match) nums.push(i);
//     }
//     return nums.length;  
};