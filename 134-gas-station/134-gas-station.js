/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let beforeStart = -2;
    let minGas = Infinity;
    let gasTotal = 0;
    
    for(let i in gas){
        // let thisLoss = cost[i] - gas[i];
        // if(thisLoss >= biggestLoss){
        //     biggestLoss = thisLoss;
        //     beforeStart = parseInt(i);
        // }
        gasTotal += gas[i];
        gasTotal -= cost[i];
        if(gasTotal<=minGas){
            minGas = gasTotal;
            beforeStart = parseInt(i);
        }
    }
    
    
    if(gasTotal<0) return -1
    if(beforeStart === gas.length-1) beforeStart = -1;
    return beforeStart+1;
};