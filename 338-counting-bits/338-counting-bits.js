/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    
    memo = [];
    
    function binaryOnes(j){
        let ans = 0;
        while (j) {
            if(j%2) ans++
            j = Math.floor(j / 2);
            
            if(memo[j]!==undefined) return memo[j] + ans;
            
        }
        return ans;
    }
    
    for(let i=0;i<=n;i++){
        let j=i; 
        memo.push(binaryOnes(j));
    }
    return memo;
};


