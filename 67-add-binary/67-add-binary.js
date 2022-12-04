/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    const digitsA = a.split('').map(n=>parseInt(n)).reverse();
    const digitsB = b.split('').map(n=>parseInt(n)).reverse();

    let place = 0;
    let carry = 0;
    let answer = '';
    
    while(digitsA[place] !== undefined || digitsB[place] !== undefined || carry){
        let sum = (digitsA[place] || 0) + (digitsB[place] || 0) + carry;
        
        if(sum > 1){
            carry = 1;
        } else {
            carry = 0;
        }
        
        if(sum % 2 === 1){
            answer = 1 + answer;
        } else {
            answer = 0 + answer;
        }
        
        
        place++;
    }
    return answer || '0';
};