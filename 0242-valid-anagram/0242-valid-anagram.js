/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const sChars = {};
    const tChars = {};
    
    for(let char of s){
        sChars[char] || (sChars[char] = 0);
        sChars[char]++;
    }
    
    for(let char of t){
        tChars[char] ||= 0;
        tChars[char]++;
    }
    
    for(let key of Object.keys(sChars)){
        if(sChars[key] !== tChars[key]){
            return false;
        }
    }
    return Object.keys(sChars).length === Object.keys(tChars).length;
};