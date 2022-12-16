/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let res = 0;
    let palindromes = new Set;
    palindromes.add('');
    for(let j=0;j<s.length;j++){
        let i=j;
        while(i>-1){
            if(s[i]===s[j] && palindromes.has(s.slice(i+1,j))){
                palindromes.add(s.slice(i,j+1));
                res++;
            }
            i--;
        }
    }
    return res;
};