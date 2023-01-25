/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const ans = [];
    const seen = new Set;
    
    function backtrack(combination,target){
        if(target===0){
            combination.sort()
            if(!seen.has(combination.toString())){
                seen.add(combination.toString())
                ans.push(combination);
            }
            return;
        }
        
        if(target<0){
            return;
        }
        
        for(let candidate of candidates){
            backtrack([...combination,candidate], target - candidate);
        }
    }
    backtrack([],target);
    return ans;
};