/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy;
    let profit = 0;
    prices.forEach((price)=>{
        if( buy === undefined || price < buy ){ buy = price }
        if( price - buy > profit ){
            profit = price - buy;
        }
    });
    
    return profit
};