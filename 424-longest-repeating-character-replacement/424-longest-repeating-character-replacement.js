/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let counts = {};
    let left=0,right=-1;res=0;
    
    while(right<s.length){
        let most = Math.max(...Object.values(counts),0);
        
        if(right-left < k+most){
            right++;
            if(!counts[s[right]]) counts[s[right]] = 0;
            counts[s[right]]++;
            
        } else {
            counts[s[left]]--;
            left++;
        }
        
        
        res = Math.max(res,Math.min(most+k,right-left));
    }
    return res;
};