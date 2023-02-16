/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    let arr = new Array(n).fill(true);
    let count = 0;
    
    for(let i=2;i<n;i++){
        if(arr[i]) count++;
        for(let j=i*i;j<n;j+=i){
            arr[j] = false;
        }
    }
    return count;
};