/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let res = ''
    let nums = '0123456789';
    
    let i = 0;
    let repeats = 0;
        
    while(!nums.includes(s[i]) && s[i]){
        i++;
    }
    
    res += s.slice(0,i);
    
    if(i===s.length) return res;
    
    while(nums.includes(s[i])){
        repeats *= 10;
        repeats += parseInt(s[i]);
        i++;
    } 
    
    let j = i;
    let openBrackets = 1;
    while(openBrackets > 0){
        j++;
        if(s[j]==='[') openBrackets++;
        if(s[j]===']') openBrackets--;
    }

    for(let k=0;k<repeats;k++){
        res += decodeString(s.slice(i+1,j));
    }
    
    res += decodeString(s.slice(j+1));
    
    return res;
};