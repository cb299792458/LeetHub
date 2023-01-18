/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(costs) {
    let price = 0;
    let differences = [];
    for(let cost of costs){
        price += cost[0];
        differences.push(cost[0]-cost[1]);
    }
    differences.sort((a,b)=>b-a);
    for(let i=0;i<costs.length/2;i++){
        price-=differences[i];
    }
    return price;
};