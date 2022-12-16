/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount, memo = {}) {
    if(amount===0) return 0;
    if(amount<0) return -1;
    
    // check the memo
    if(memo[amount]) return memo[amount];
    
    // sort to try biggest coins first
    // coins = coins.sort((a,b)=>{return b-a})
    
    let minimumCoins = Infinity;
    
    // remove biggest coin
    // let coinsCopy = coins.slice();
    
    
    for(let coin of coins){
        
        let current = 1 + coinChange(coins, amount-coin,memo);
        memo[amount-coin] = current-1;
        if(current !== 0 && current < minimumCoins){
            minimumCoins = current;
        }
    }
    // console.log(memo)
    return minimumCoins === Infinity ? -1 : minimumCoins;
    
};