/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {

    let ans = [];
    
    let counts = {};
    for(let char of p){
        if(!counts[char]) counts[char] = 0;
        counts[char]++;
    }
    
    
    for(let right=0;right<s.length;right++){
        let left = right - p.length;
        
        if(!counts[s[right]]) counts[s[right]] = 0;
        counts[s[right]]--;
        
        if(left>=0){
            if(!counts[s[left]]) counts[s[left]] = 0;
            counts[s[left]]++;
        }
        
        if(Object.values(counts).every(ele=>ele===0)){
            ans.push(left+1)
        }
    }
    
    return ans;
};