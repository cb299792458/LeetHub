/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let combos = [];
    const dfs = (target, nums = []) => {
        candidates.forEach((num)=>{
            let thisTarget = target;
            thisNums = nums.concat([num]);
            thisTarget -= num;
            if(thisTarget < 0){return}
            if(thisTarget === 0){
                combos.push(thisNums.sort());
                return;
            }
            dfs(thisTarget,thisNums);
        });
    };
    
    dfs(target,[]);
    console.log(combos);
    // return combos.entries();
    
    let ans = [];
    let alreadyIn = [];
    for(let combo of combos){
        if(!alreadyIn.includes(JSON.stringify(combo))){
            alreadyIn.push(JSON.stringify(combo));
            ans.push(combo);
        }
    }
    
    return ans;
};