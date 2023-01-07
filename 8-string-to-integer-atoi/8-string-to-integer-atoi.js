/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let array = s.split('')
    let sign = 1;
    
    while(' '.includes(array[0])){
        array.shift();
    }
    
    if(array[0]==='-' || array[0]==='+'){
        if(array[0]==='-') sign = -1;
        array.shift();
    }

    let num = 0;
    for(let char of array){
        if(!'1234567890'.includes(char)) break
        num = num * 10 + parseInt(char);
    }
    
    let ans = sign * num;
    if(-(2**31) > ans) return -(2**31);
    if(ans > (2**31)-1) return 2**31-1;
    return ans;
};