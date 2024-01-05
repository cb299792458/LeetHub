var isValid = function(s) {
    const stack = [];
    
    for (let char of s) {
        if ( ['(', '{', '['].includes(char)) {
            stack.push(char);
        } else {
            const last = stack[stack.length-1];
            if (char===')' && last==='(') {
                stack.pop();
            } else if (char==='}' && last==='{') {
                stack.pop();
            } else if (char===']' && last==='[') {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    
    // if (stack.length>0) {
    //     return false;
    // }
    // return true;
    return stack.length===0
};