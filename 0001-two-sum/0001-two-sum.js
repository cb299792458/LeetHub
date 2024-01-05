var twoSum = function(nums, target) {
    const N = nums.length;
    
    for(let i=0; i<N; i++){
        for(let j=0; j<N; j++){
            if(i===j){
                continue;
            }
            
            if(nums[i]+nums[j]===target){
                return [i,j];
            }
        }
    }
};