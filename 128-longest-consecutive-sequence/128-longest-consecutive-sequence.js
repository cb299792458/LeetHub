/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let hash = new Set(nums);
    let maxCount = 0;
    
    nums.forEach((num) => {
        if(hash.has(num-1)){return}
        
        let count = 0;
        let start = num;
        while(hash.has(num)){
            count ++;
            num ++;
        }
        maxCount = Math.max(maxCount,count);
    });

    return maxCount;
};