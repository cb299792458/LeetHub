/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    const dp = new Array(366).fill(0);
    days = new Set(days);
    
    for(let i=1;i<366;i++){
        if(days.has(i)){
            let buyToday = dp[i-1] + costs[0];
            
            let sevenDaysAgo = i > 7 ? dp[i-7] : 0;
            sevenDaysAgo += costs[1];
            
            let thirtyDaysAgo = i > 30 ? dp[i-30] : 0;
            thirtyDaysAgo += costs[2];
            
            dp[i] = Math.min(buyToday, sevenDaysAgo, thirtyDaysAgo);
        } else {
            dp[i] = dp[i-1];
        }
    }
    // console.log(dp)
    return dp.at(-1);
};