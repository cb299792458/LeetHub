/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points = points.sort((a,b)=>{
        return a[1] - b[1];
    })
    // console.log(points);
    
    let arrows = [-Infinity];
    for(let i=0;i<points.length;i++){
        if(arrows.at(-1)>points[i][1] || arrows.at(-1)<points[i][0]){
            arrows.push(points[i][1])
        }
    }
    // console.log(arrows);
    
    return arrows.length-1
};