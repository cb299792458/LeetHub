/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    
    // make a heap, much faster
    const queue = new MaxPriorityQueue();
    
    for (stone of stones) queue.enqueue(stone)
    
    while (queue.size() > 1) {
        let first = queue.dequeue().element;
        let second = queue.dequeue().element;
        if (first !== second) queue.enqueue(first-second)
    }
    
    return queue.size() === 0 ? 0 : queue.front().element

    
    while(stones.length>1){
        stones = stones.sort((a,b)=>{return a-b});
        console.log(stones);
        let x = stones.pop();
        let y = stones.pop();
        if(x === y) continue;
        stones.push(x-y);
    }
    return stones[0] ? stones[0] : 0;
};