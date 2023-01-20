/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findSubsequences = function(nums) {
    let res = [];
    
    const subsFromStart = function(start){
        let res = [];
        let first = nums[start];
        for(let i=start+1;i<nums.length;i++){
            let temp = [];
            let current = nums[i];
            if(current>=first) temp.push([first,current]);
            for(let sub of res){
                if(current>=sub.at(-1)){
                    temp.push(sub.concat([current]))
                }
            }
            res = res.concat(temp);

        }
        return res
    } 
        
    for(let i = 0; i<nums.length; i++){
        res = res.concat(subsFromStart(i))
    }
    
    let finalRes = [];
    let uniqueRes = new Set();
    for(let sub of res){
        let str = `${sub}`;
        if(!uniqueRes.has(str)){
            uniqueRes.add(str);
            finalRes.push(sub);
        }
    }

    return finalRes;
};