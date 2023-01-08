/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = '';

    for(let i=0;i<strs[0].length;i++){
        let c=strs[0][i];
        for(let str of strs){
            if(c!==str[i]) return prefix;
        }
        prefix += c;
    }
    
    return prefix;
};