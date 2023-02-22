/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    function checkWeight(w){
        let capacity = w;
        let ships = 1;
        for(let weight of weights){
            if(weight>w) return false;
            if(capacity>=weight){
                capacity -= weight;
            } else {
                ships++;
                capacity = w - weight;
            }
        }
        return ships <= days;
    }
    checkWeight(16)
    
    let left = Math.max(...weights);
    let right = weights.reduce((num,sum) => num+sum );
    let res;
    while(left<=right){
        let mid = Math.floor((left+right)/2);
        console.log(left,right,mid)
        if(checkWeight(mid)){
            res = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }
    return res;
};