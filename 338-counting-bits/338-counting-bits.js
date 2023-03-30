/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    
    memo = [];
    
    function binary(j){
        let ans = 0;
        while (j) {
          if(j%2) ans++
          j = Math.floor(j / 2);
        }
        return ans;
    }
    
    for(let i=0;i<=n;i++){
        let j=i; 
        memo.push(binary(j));
    }
    return memo;
};


