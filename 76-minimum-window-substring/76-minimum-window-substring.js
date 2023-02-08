/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let counts = {};
    for(let char of t){
        if(!counts[char]) counts[char] = 0;
        counts[char]++;
    }
    let correctCounts = 0;    
    
    const valid = () => correctCounts === Object.keys(counts).length;
    let window = false;
    
    let left = 0, right = 0;

    if(counts[s[right]]!==undefined){
        counts[s[right]]--;
        if(counts[s[right]]===0) correctCounts++;
    }    
    while(left < s.length){
        if(valid()){
            if(!window||window[1]-window[0]>right-left) window=[left,right];
            if(counts[s[left]]!==undefined){
                counts[s[left]]++;
                if(counts[s[left]] === 1) correctCounts--;
            }
            left++
        } else if(right !== s.length-1){
            right++;
            if(counts[s[right]]!==undefined){
                counts[s[right]]--;
                if(counts[s[right]]===0) correctCounts++;
            }
        } else {
            if(counts[s[left]]!==undefined){
                counts[s[left]]++;
                if(counts[s[left]] === 1) correctCounts--;
            }
            left++
        }
        
    }
    return window ? s.slice(window[0],window[1]+1) : ''
};