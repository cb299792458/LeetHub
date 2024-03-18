/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points = points.sort((a,b)=>{
        return a[1] - b[1];
    })
    
    let arrows = [-Infinity];
    for(let i=0;i<points.length;i++){
        if(arrows.at(-1)<points[i][0]){
            arrows.push(points[i][1])
        }
    }
    
    return arrows.length-1
};