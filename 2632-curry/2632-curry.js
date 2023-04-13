/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    let args = [];
    let num = fn.length;
    return function curried(...arg) {
        args.push(...arg);
        if (args.length === num) return fn(...args);
        return curried;
    }
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
