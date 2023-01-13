/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const res = [];
    const set = new Set;
    
    for(let i=0;i<nums.length;i++){
        const first = nums[i];
        const map = {};
        for(let j=i+1;j<nums.length;j++){
            const second=nums[j];
            if(map[second]===undefined){
                map[0-first-second]=second;
            } else{
                let ans = [first, second, map[second]];
                ans = ans.sort((a,b)=>a-b);
                
                if(!set.has(`${ans[0]},${ans[1]},${ans[2]}`)){
                    res.push(ans);
                    set.add(`${ans[0]},${ans[1]},${ans[2]}`)
                }
                
            }
        }
    }
    
    return res;
    
};