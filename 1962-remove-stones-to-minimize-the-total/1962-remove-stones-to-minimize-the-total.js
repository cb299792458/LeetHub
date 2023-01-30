/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */

var minStoneSum = function(piles, k) {
    let queue = new MaxPriorityQueue;
    for(let pile of piles){
        queue.enqueue(pile);
    }
    for(let i=0;i<k;i++){
        let stones = queue.dequeue().element;
        stones -= Math.floor(stones/2);
        queue.enqueue(stones);
    }
    
    // finish by adding them all up
    let total = 0;
    while(!queue.isEmpty()){
        total += queue.dequeue().element;
    }
    return total;
};