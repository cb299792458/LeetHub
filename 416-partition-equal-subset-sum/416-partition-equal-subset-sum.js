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


