/**
 * @param {number} lo
 * @param {number} hi
 * @param {number} k
 * @return {number}
 */
var getKth = function(lo, hi, k) {    
    let powerMemo = {1: 0};
    
    function power(n){
        let count = 0;
        let original = n;
        while(true){
            // console.log(powerMemo[n])
            if(powerMemo[n] !== undefined){
                count += powerMemo[n];
                powerMemo[original] = count;
                return count;
            }
            
            
            count++;
            if(n%2===0){
                n /= 2;
            } else {
                n = 3*n+1
            }
        }
        
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