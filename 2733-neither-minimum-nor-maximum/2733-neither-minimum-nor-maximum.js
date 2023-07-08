/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    // [3,2,1,4]
    
    let minimum=nums[0];
    let maximum=nums[0];
    
    for(let i=0; i<nums.length; i++){
        let num = nums[i];
        
        if(num<minimum){
            minimum=num;
        }
        if(num>maximum){
            maximum=num;
        }
    }
    
    // console.log('Minimum is', minimum);
    // console.log('Maximum is', maximum);
    
    for(let i=0; i<nums.length; i++){
        let num2 = nums[i];
        if(num2<maximum && num2>minimum){
            return nums[i];
        }
    }
    
    return -1;
    
};