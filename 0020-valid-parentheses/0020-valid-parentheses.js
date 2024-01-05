var isValid = function(s) {
    const stack = [];
    
    for (let char of s) {
        if (['(', '[', '{'].includes(char)) {
            stack.push(char);
        } else {
            const last = stack[stack.length-1];
            if (last==='(' && char===')') {
                stack.pop();
            } else if (last==='{' && char==='}') {
                stack.pop();
            } else if (last==='[' && char===']') {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    if (stack.length>0) {
        return false;
    }
    return true;
};