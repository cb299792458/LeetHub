/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const parens = {'(':')', '[':']', '{':'}'};
    let ans = true;
    let chars = [];
    s.split('').forEach((c)=>{
        if(parens[c]){
            chars.push(c);
        } else {
            if(parens[chars[chars.length-1]] === c){
                chars.pop();
            } else {
                ans = false;
            }
        }
        
    })
    return ans && chars.length === 0;
};