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
        gasTotal += gas[i] - cost[i];
        if(gasTotal<=minGas){
            minGas = gasTotal;
            beforeStart = parseInt(i);
        }
    }
    
    
    if(gasTotal<0) return -1
    if(beforeStart === gas.length-1) return 0;
    return beforeStart+1;
};