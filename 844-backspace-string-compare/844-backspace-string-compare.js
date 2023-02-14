/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let stringS = [];
    let stringT = [];
    
    for(let char of s){
        if(char==='#') stringS.pop();
        else stringS.push(char);
    }
    for(let char of t){
        if(char==='#') stringT.pop();
        else stringT.push(char);
    }
    
    return stringS.join()===stringT.join();
};