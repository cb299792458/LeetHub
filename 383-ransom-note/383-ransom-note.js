/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let missing = false;
    let letters = magazine.split('');
    let ransomLetters = ransomNote.split('');
    while(!missing && ransomLetters.length){
        let char = ransomLetters.shift();
        let index = letters.indexOf(char);
        console.log( char, index );
        if(index === -1){
            missing = true;
        } else {
            letters.splice(index,1);
        }
    }
    return !missing;
};