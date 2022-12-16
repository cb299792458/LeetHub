/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let frequencies = {}
    for(let num of nums){
        if(!frequencies[num]){
            frequencies[num]=[1]
        } else {
            frequencies[num]++;
        }
    }
    
    let integersByFrequency = {};
    for(let num in frequencies){
        if(!integersByFrequency[frequencies[num]]){
            integersByFrequency[frequencies[num]] = [];
        }
        integersByFrequency[frequencies[num]].push(num);
    }
    // console.log(integersByFrequency)
    
    let ans = [];
    let j=nums.length;
    while(ans.length<k){
        if(integersByFrequency[j]){
            ans = ans.concat(integersByFrequency[j]);
        }
        j--
    }
    return ans;
};