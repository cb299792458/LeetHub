/**
 * @param {number} n
 * @return {number}
 */
let ans = {0: 0, 1: 1}
var fib = function(n) {
    if (n in ans) return ans[n];
    const res = fib(n-1) + fib(n-2)
    ans[n] = res
    return res
};