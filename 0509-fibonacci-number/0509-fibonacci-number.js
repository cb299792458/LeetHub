/**
 * @param {number} n
 * @return {number}
 */
const answers = {0: 0, 1: 1}
var fib = function(n) {
    if (n in answers) {
        return answers[n];
    }
    
    const result = fib(n-1) + fib(n-2);
    answers[n] = result;
    return result
};