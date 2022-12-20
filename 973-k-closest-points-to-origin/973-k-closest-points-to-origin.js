/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    const sorted = points.sort((a,b)=>{
        return distance(a[0],a[1]) - distance(b[0],b[1]);
    });
    return sorted.slice(0,k);
};

function distance(x,y){
    return Math.sqrt(x*x+y*y);
}