/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    intervals.push(newInterval);
    intervals.sort((a,b)=>{
        return a[0] - b[0];
    });
    
    return merge(intervals);
    
};

function merge(intervals) {
    console.log(intervals)
    let merged = true;
    while(merged === true){
        merged = false;
        let newArray = [];
        for(let i = 0; i < intervals.length; i++){
            if(intervals[i+1] && intervals[i][1] >= intervals[i+1][0]){
                newArray.push([intervals[i][0],Math.max(intervals[i+1][1],intervals[i][1])]);
                merged = true;
                i += 1;
            } else {
                newArray.push(intervals[i]);
            }
        }
        intervals = newArray;
    }
    return intervals;
}