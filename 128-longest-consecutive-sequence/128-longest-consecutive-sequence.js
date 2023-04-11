/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let hash = new Set(nums);
    let maxCount = 0;
    
    for(let num of nums){
        if(hash.has(num-1)) continue;
        
        let i = num;
        while(hash.has(i)) i++
        maxCount = Math.max(maxCount, i-num)
    }

    return maxCount;
};