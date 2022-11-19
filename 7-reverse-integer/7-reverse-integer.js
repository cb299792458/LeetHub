/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let negative = x < 0;
    let str = '' + x;
    if(negative){
        str = str.slice(1);
    }
    let reversed = '';
    for(let i=str.length-1;i>=0;i--){
        reversed += str[i];
    }
    if(negative){
        reversed = -reversed;
    }
    if(Math.abs(reversed) < 2**31){
        return reversed;   
    }
    return 0;
};