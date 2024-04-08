/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const counts = {};
    for (const c of magazine) {
        counts[c] ||= 0;
        counts[c]++;
    }
    for (const c of ransomNote) {
        if (counts[c] === undefined || counts[c] === 0) {
            return false;
        }
        counts[c]--;
    }
    return true;
};