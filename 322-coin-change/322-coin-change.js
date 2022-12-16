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

    let minimumCoins = Infinity;
    
    for(let coin of coins){
        
        let current = 1 + coinChange(coins, amount-coin,memo);
        memo[amount-coin] = current-1;
        if(current !== 0 && current < minimumCoins){
            minimumCoins = current;
        }
    }

    return minimumCoins === Infinity ? -1 : minimumCoins;
    
};