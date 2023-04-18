/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    word1=word1.split('').reverse();
    word2=word2.split('').reverse();
    
    res=[];
    while(word1.length && word2.length){
        res.push(word1.pop());
        res.push(word2.pop());
    }
    return [...res,...word1.reverse(),...word2.reverse()].join('');
};