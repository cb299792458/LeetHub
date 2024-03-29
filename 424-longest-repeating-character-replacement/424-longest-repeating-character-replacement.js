/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let counts = {};
    let left=0,right=-1,res=0;
    let most = 0;
    while(right<s.length){
        
        if(right-left < k+most){
            right++;
            if(!counts[s[right]]) counts[s[right]] = 0;
            counts[s[right]]++;
            most = Math.max(most,counts[s[right]])
            
        } else {
            counts[s[left]]--;
            left++;
        }
        
        res = Math.max(res,right-left);
    }
    return res;
};