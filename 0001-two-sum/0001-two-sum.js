var twoSum = function(nums, target) {
    const N = nums.length;
    
    const indexOfPrev = {};
    for(let i=0; i<N; i++){
        const curr = nums[i];
        const diff = target - curr;
        if(diff in indexOfPrev){
            return [i, indexOfPrev[diff]]
        }
        
        indexOfPrev[curr] = i;
    }
    // console.log(indexOfPrev)
};