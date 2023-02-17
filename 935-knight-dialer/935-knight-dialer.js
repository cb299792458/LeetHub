var knightDialer = function(n){
    // a hashmap for each number, possible places to go from there
    // This is called an adjacency list, example: 6 is adjacent to 0, 1, and 7
    
    let mod = 10**9 + 7;
    let options = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    let dp = new Array(10).fill(1);
    
    for(let i=1;i<n;i++){
        let newDp = new Array(10).fill(0);
        for(let j=0;j<10;j++){
            for(let option of options[j]){
                newDp[j] = (newDp[j] + dp[option])%mod;
            }
        }
        dp = newDp
    }
    // console.log(dp)
    return dp.reduce((sum,num) => sum+num) % mod;
}
