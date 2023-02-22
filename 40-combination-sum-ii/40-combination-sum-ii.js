// /**
//  * @param {number[]} candidates
//  * @param {number} target
//  * @return {number[][]}
//  */
// var combinationSum2 = function(candidates, target) {
//     const ans = [];
//     const anset = new Set();
    
//     const backtrack = (nums, index, t) => {
//         console.log(nums,index);
//         if(t<0) return;
//         if(t===0 && !anset.has(nums.join(''))){
//             anset.add(nums.join(''));
//             ans.push(nums);
//             return;
//         }
                
//         for(let i=index;i<candidates.length;i++){
//             backtrack([...nums,candidates[i]],i+1,t-candidates[i])
//         }
//     };
    
//     backtrack([],0,target);
//     return ans;
// };
var combinationSum2 = function(c, target) {
    c.sort((a,b)=>a-b)
    let res = []

    let iterate = (index,sum,temp) =>{
        if(sum>target) return;
        if(sum == target){
            res.push(temp)
            return;
        }
        // 1 1 2 5 6 7 10 
        for(let i =index; i<c.length;i++){
            if(i != index && c[i] == c[i-1]) continue;
            iterate(i+1,sum+c[i],[...temp,c[i]])
        }
    }
    iterate(0,0,[])
    return res;
};