/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const ans = [];
    function backtrack(opens, closes, combo){
        if(opens===0&&closes===n){
            ans.push(combo);
            return;
        }
        if(opens>0){
            backtrack(opens-1,closes+1,combo+')');
        }
        if(opens+closes<n){
            backtrack(opens+1,closes,combo+'(');
        }
        
    };
    
    backtrack(0,0,'');
    return ans;
    
};