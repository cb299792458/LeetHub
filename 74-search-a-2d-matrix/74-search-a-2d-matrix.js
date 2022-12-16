/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if(target<matrix[0][0]) return false;
    let top = 0;
    let bot = matrix.length-1;
    while(top < bot){
        let mid = Math.floor((top+bot)/2);
        // console.log(top,bot,mid,matrix[mid][0],target)
        if(target<matrix[mid][0]){
            // console.log('hit')
            bot = mid-1;
        } else if(target>matrix[mid].at(-1)){
            top = mid+1;
        } else {
            top = mid;
            bot = mid;
        }
    }
    // console.log(top);
    const sub = matrix[top];
    let left = 0;
    let right = sub.length-1;
    if(target<sub[left]) return false;
    while(left < right){
        
        let mid = Math.floor((left+right)/2);
        // console.log(left,right,mid)
        if(sub[mid]===target) return true;
        if(sub[mid]<target) left = mid+1;
        if(sub[mid]>target) right = mid-1;
    }
    return sub[left]===target;
};