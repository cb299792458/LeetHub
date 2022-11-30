/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let counts = {};
    s.split('').forEach((c)=>{
        if(!counts[c]){
            counts[c] = 1;
        } else {
            counts[c]++;
        }
    });
    // console.log(counts)
    let extra = 0;
    let length = 0;
    Object.values(counts).forEach((num)=>{
        if(num % 2 === 1){
            extra = 1;
            length += num-1;
        } else {
            length += num;
        }
    });
    return length + extra;
};