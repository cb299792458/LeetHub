/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {

    let dp = new Array(s.length);
    let longest = '';
    
    
    for(let i=0;i<s.length;i++){
        let oddCurrent = s[i];
        for(let j=1;;j++){
            if(s[i-j] && s[i+j] && s[i-j] === s[i+j]){
                oddCurrent = s[i-j] + oddCurrent + s[i+j];
            } else {
                break;
            }
        }
        if(longest.length < oddCurrent.length) longest = oddCurrent;
        
        let evenCurrent = '';
        for(let k=0;;k++){
            if(s[i-k] && s[i+k+1] && s[i-k] === s[i+k+1]){
                evenCurrent = s[i-k] + evenCurrent + s[i+k+1];
            } else {
                break;
            }
        }
        if(longest.length<evenCurrent.length) longest = evenCurrent;
        
    }
    return longest
};