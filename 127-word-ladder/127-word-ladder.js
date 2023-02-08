/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    wordList = new Set(wordList);
    if(!wordList.has(endWord)) return 0;
    
    let currentWords = new Set([beginWord]);
    let steps = 2;
    const alphabet = 'qwertyuiopasdfghjklzxcvbnm';
    
    while(currentWords.size){
        let temp = new Set();
        for(let word of currentWords){
            wordList.delete(word);
    
            for(let i=0;i<word.length;i++){
                for(let letter of alphabet){
                    let newWord = word.slice(0,i) + (letter) + word.slice(i+1);
                    // console.log(newWord)
                    if(newWord===endWord) return steps;
                    if(wordList.has(newWord)) temp.add(newWord);
                }
            }
        }
        currentWords = temp;
        steps++;
    }
    return 0;
};