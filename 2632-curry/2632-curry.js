/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    let curriedArgs = [];
    let numArgs = fn.length;
    return function _curried(...args) {
        curriedArgs.push(...args);
        if (curriedArgs.length === numArgs) return fn(...curriedArgs);
        return _curried;
    }
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
