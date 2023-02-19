/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let words = s.split(' ');
    // console.log(words)
    for(let i=words.length-1;;i--){
        if(words[i]) return words[i].length
    }
};