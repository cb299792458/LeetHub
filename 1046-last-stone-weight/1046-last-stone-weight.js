/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    
    // make a heap, much faster
    
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