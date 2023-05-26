/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    if(!n) return arr;
    
    const res = []
    for(let ele of arr){
        if(!Array.isArray(ele)){
            res.push(ele);
        } else {
            res.push(...flat(ele,n-1));
        }
    }
    return res;
};