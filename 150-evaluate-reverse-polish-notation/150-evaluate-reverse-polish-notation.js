/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    // console.log(parseInt(tokens[0]))
    let nums = [];

    for(let str of tokens){
        if(['+','-','*','/'].includes(str)){
            // console.log(str)
            let first = nums.pop();
            let second = nums.pop();
            let result;
            switch(str){
                case '+':
                    result = first + second;
                    break;
                case '-':
                    result = second - first;
                    break;
                case '*':
                    result = first * second;
                    break;
                case '/':
                    result = second / first;
                    if(result > 0){
                        result = Math.floor(result);
                    } else {
                        result = Math.ceil(result);
                    }
                    break;
            }
            nums.push(result);
        } else {
            nums.push(parseInt(str));
        }
    console.log(nums)
    }
    return nums[0]
};