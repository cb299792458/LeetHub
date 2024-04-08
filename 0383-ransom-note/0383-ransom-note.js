/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const counts = {}; // key: character, val: count for that character
    for (let c of magazine) {
        if (counts[c] === undefined) {
            counts[c] = 0;
        }
        counts[c]++;
    }
    
    for (let c of ransomNote) {
        if (counts[c] === undefined || counts[c] === 0) {
            return false;
        }
        counts[c]--;
    }
    return true
};