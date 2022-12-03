/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let counts = {};
    s.split('').forEach((char)=>{
        counts[char] = counts[char] ? counts[char] + 1 : 1;
    });
    let countArr = Object.entries(counts).sort((a,b)=>{return b[1] - a[1]})
    let ans = '';
    countArr.forEach((arr)=>{
       for(let i = 0; i < arr[1]; i++){
           ans += arr[0];
       } 
    });
    return ans;
};