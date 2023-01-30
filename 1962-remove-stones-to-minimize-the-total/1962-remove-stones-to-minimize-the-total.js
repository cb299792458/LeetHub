/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */

var minStoneSum = function(piles, k) {
    let queue = new MaxPriorityQueue;
    let total = 0;
    for(let pile of piles){
        queue.enqueue(pile);
        total += pile;
    }
    for(let i=0;i<k;i++){
        let stones = queue.dequeue().element;
        let removed = Math.floor(stones/2);
        total -= removed;
        stones -= removed;
        queue.enqueue(stones);
    }
    
    return total;
};