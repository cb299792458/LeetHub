var twoSum = function(nums, target) {
    const N = nums.length;
    const indexOfSeen = new Map();
    
    for(let i=0; i<N; i++){
        let difference = target - nums[i];

        if(indexOfSeen.has(difference)){
            console.log('sdf')
            return [i,indexOfSeen.get(difference)];
        }
        
        indexOfSeen.set(nums[i],i)
    }
    
    console.log(indexOfSeen);
};