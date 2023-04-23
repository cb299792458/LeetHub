/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = [];
    for(let i=0;i<arr.length;i++){
        let ele = arr[i];
        if(fn(ele,i)) res.push(ele);
    }
    return res;
};