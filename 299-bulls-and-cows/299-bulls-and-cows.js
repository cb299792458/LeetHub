/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let bulls = 0;
    let cows = 0;
    let s = {};
    let g = {};
    for(let i=0;i<secret.length;i++){
        if(secret[i]===guess[i]){
            bulls++;
        } else {
            s[secret[i]] ||= 0;
            s[secret[i]]++;
            g[guess[i]] ||= 0;
            g[guess[i]]++;
        }
    }
    for(let key of Object.keys(s)){
        if(g[key]) cows += Math.min(s[key],g[key])
    }
    
    return bulls + 'A' + cows + 'B'
};