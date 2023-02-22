/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    const ans = [];
    // const anset = new Set();
    candidates.sort();
    
    const backtrack = (nums, index, t) => {
        if(t<0) return;
        if(t===0){
            // anset.add(nums.join(''));
            ans.push(nums);
            return;
        }
                
        for(let i=index;i<candidates.length;i++){
            if(i!==index && candidates[i-1]===candidates[i]) continue;
            backtrack([...nums,candidates[i]],i+1,t-candidates[i])
        }
    };
    
    backtrack([],0,target);
    return ans;
};