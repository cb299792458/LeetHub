/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals = intervals.sort((a,b)=>a[0]-b[0]);
    intervals.push([Infinity,Infinity])
    
    let res = [];
    let prev;
    for(let interval of intervals){
        if(!prev){
            prev = interval;
            continue;
        }
        
        if(prev[1]<interval[0]){
            res.push(prev);
            prev = interval;
            continue;
        } else if(prev[1]<interval[1]){
            prev[1] = interval[1];
        }
    }
    
    return res;
};