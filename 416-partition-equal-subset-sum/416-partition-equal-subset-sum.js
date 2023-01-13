/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    let sum = 0;
    for(let num of nums){
        sum += num;
    }
    
    let half;
    if(sum%2===0){
        half = sum/2;
    } else {
        return false;
    }

    // return canSum(nums,half);
    let possibilities = new Set;
    possibilities.add(0);
    for(let num of nums){
        let temp = new Set;
        for(let pos of possibilities){
            if(pos === half || pos + num === half){
                return true;
            }
            temp.add(pos);
            temp.add(pos + num);
        }
        possibilities = temp;
    }
    return false;
};

// const canSum = (originalNums,total) => {
//     let nums = originalNums.slice();
//     // console.log(nums,total)
//     if(total<0) return false;
//     if(total===0) return true;
//     if(!nums.length) return false;
    
//     const num = nums.pop();
//     return(canSum(nums,total-num) || canSum(nums,total));
// }

