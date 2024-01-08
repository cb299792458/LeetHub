/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    counts = {};
    for (let char of s) {
        counts[char] ||= 0;
        counts[char]++;
    }
    for (let char of t) {
        counts[char] ||= 0;
        counts[char]--;
    }
    return Object.values(counts).every(c => c===0);
};