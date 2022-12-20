/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let left = 0;
    let right = 0;
    
    let letters = new Set;
    let length = 0;
    
    while(right < s.length){
        if(!letters.has(s[right])){
            letters.add(s[right]);
            right++;
        } else {
            letters.delete(s[left]);
            left++;
        }
        length = Math.max(length,letters.size);
    }
    
    return length;
};