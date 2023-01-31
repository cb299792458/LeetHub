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
    
    return queue.isEmpty() ? 0 : queue.front().element

};