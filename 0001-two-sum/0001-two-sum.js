var twoSum = function(nums, target) {
    const N = nums.length;
    const indexOfPrev = {}
    
    for(let i=0; i<N; i++){
        const diff = target - nums[i];
        if(diff in indexOfPrev){
            return [indexOfPrev[diff], i];
        }
        indexOfPrev[nums[i]] = i
    }
    
};