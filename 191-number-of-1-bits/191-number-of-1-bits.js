/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let str = n.toString(2);
    let count = 0;
    for(let char of str){
        if(char==='1') count++
    }
    return count
};