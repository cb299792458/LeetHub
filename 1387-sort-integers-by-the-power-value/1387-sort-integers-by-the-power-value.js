/**
 * @param {number} lo
 * @param {number} hi
 * @param {number} k
 * @return {number}
 */
var getKth = function(lo, hi, k) {    
    function power(n){
        let count = 0;
        while(n>1){
            count++;
            if(n%2===0){
                n /= 2;
            } else {
                n = 3*n+1
            }
        }
        return count;
    }
    
    
    let arr = [];
    for(let i = lo; i <= hi; i++) arr.push(i);
    
    
    arr.sort((a,b)=>{
        let pa = power(a);
        let pb = power(b);
        if(pa===pb) return a-b;
        return pa-pb;
    });
    
    return arr[k-1];
};