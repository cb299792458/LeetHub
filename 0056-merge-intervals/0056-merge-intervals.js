var merge = function(intervals) {
    intervals.sort((a,b)=>a[0]-b[0]);
    intervals.push([Infinity,Infinity])
    
    let res = [];
    let prev;
    for(let interval of intervals){
        
        prev ||= interval
        
        if(prev[1]<interval[0]){
            res.push(prev);
            prev = interval;
        } else if(prev[1]<interval[1]){
            prev[1] = interval[1];
        }
    }
    
    return res;
};