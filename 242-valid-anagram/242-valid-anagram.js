/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {

    let counts = {};
    for(let c of s){
        if(counts[c] !== undefined){
            counts[c]++;
        } else {
            counts[c] = 1;
        }
    }
    for(let c of t){
        if(counts[c] !== undefined){
            counts[c]--;
        } else {
            counts[c] = -1;
        }
    }
    let nums = Object.values(counts).filter((num)=>{
        return num != 0;
    })
    return nums.length === 0;
};