/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let map = {};
    for(let i=0;i<s.length;i++){
        if(!map[s[i]]) map[s[i]] = t[i];
        else if(map[s[i]]!==t[i]) return false;
    }
    let letters = Object.values(map);
    let set = new Set(letters);
    return set.size===letters.length
};