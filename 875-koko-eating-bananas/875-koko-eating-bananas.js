/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    
    function canEat(k){
        let time = 0;
        for(let pile of piles) time += Math.ceil(pile/k);
        return time <= h;
    }
    
    let left = 1;
    let right = Math.max(...piles);
    
    while(left<right){
        let mid = Math.floor((left+right)/2);
        
        if(canEat(mid)){
            right = mid;
        } else {
            left = mid+1;
        }
    }
    
    return left;
};