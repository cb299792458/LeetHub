/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // console.log(''+x);
    let str = '' + x;
    let chars = str.split('');
    return JSON.stringify(chars) === JSON.stringify(chars.reverse())
};