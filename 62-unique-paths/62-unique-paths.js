/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let factorials = [1];
    for(let i = 1; i <= m+n-2; i++){
        factorials[i] = factorials[i-1] * i;
    }
    return (factorials[m+n-2])/(factorials[m-1]*factorials[n-1]);
};