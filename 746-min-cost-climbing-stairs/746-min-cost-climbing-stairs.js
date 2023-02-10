/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    let mins = [0,0];
    for(let i=2;i<=cost.length;i++) mins.push(Math.min(mins[i-1]+cost[i-1],mins[i-2]+cost[i-2]))
    return mins.at(-1)
};