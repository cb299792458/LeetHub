/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let temp=[];
    const res=[];
    
    for(let ele of arr){
        temp.push(ele);
        if(temp.length===size){
            res.push(temp);
            temp=[];
        }
    }
    if(temp.length) res.push(temp);
    return res;
};
