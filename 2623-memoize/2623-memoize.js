/**
 * @param {Function} fn
 */
function memoize(fn) {
    memo={}
    return function(...args) {
        if(memo[args]!==undefined) return memo[args];
        const res = fn(...args);
        memo[args] = res;
        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */