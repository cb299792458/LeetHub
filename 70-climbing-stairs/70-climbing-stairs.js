/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let answers = [];
    answers[1] = 1;
    answers[2] = 2;
    
    for(let i = 3; i <= n; i++){
        answers[i] = answers[i-1] + answers[i-2];
    }
    return answers[n];
};