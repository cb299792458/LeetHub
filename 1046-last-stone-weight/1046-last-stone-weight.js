/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    let sortedStones = stones.sort((a,b) => b - a)
    while (sortedStones.length > 1) {
        // console.log(sortedStones)
        if (sortedStones[0] === sortedStones[1]) {
            sortedStones = sortedStones.slice(2, sortedStones.length);
        } else if (sortedStones[0]>sortedStones[1]) {
            const newWeight = sortedStones[0]-sortedStones[1];
            sortedStones.splice(0, 1, newWeight);
            sortedStones.splice(1, 1);
            sortedStones.sort((a,b) => b - a)
        } 
    }
    return sortedStones;
};