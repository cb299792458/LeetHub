/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    sChars = {};
    tChars = {};
    
    for(let c of s){
        if(sChars[c]===undefined){
            sChars[c] = 0;
        }

        sChars[c]++;
    }
    
    for(let c of t){
        if(tChars[c]===undefined){
            tChars[c] = 0;
        }

        tChars[c]++;
    }
    
    for(let c of Object.keys(sChars)){
        if(sChars[c] !== tChars[c]){
            return false;
        }
    }
    
    return Object.keys(sChars).length === Object.keys(tChars).length;
};