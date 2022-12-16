/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount, memo = {}) {
    if(amount===0) return 0;
    if(amount < 0) return -1;
    if(memo[amount]) return memo[amount];
    
    let res = Infinity;
    
    for(const coin of coins){
        const newAmount = amount - coin;
        const newAns = coinChange(coins, newAmount, memo);
        if(newAns !== -1){
            res = Math.min(res,newAns+1)
        }
    }
    // console.log(memo)
    memo[amount] = res;
    return res===Infinity ? -1 : res;
};