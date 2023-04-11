/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    const stack = [];
    for(const op of operations){
        switch(op){
            case '+':
                stack.push(stack.at(-1)+stack.at(-2));
                break;
            case 'D':
                stack.push(stack.at(-1)*2);
                break;
            case 'C':
                stack.pop();
                break;
            default:
                stack.push(parseInt(op));
        }
    }
    
    return stack.reduce((a,c)=>a+c,0);
};