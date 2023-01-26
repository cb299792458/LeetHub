/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if(n==0) return 0;
    const nums = [0,1];
    for(let i=2;i<=n;i++){
        if(i%2===0){
            nums[i] = nums[i/2];
        } else {
            nums[i] = nums[Math.floor(i/2)] + nums[Math.ceil(i/2)];
        }
        
    }

    return Math.max(...nums);
};