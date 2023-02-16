var removeDuplicates = function(s, k) {
    // make a stack = []
    let stack = [];
    for(let char of s){
        let lastI = stack.length - 1
        if(stack.length > 0 && stack[lastI][0] === char){
            stack[lastI][1]++
            if(stack[lastI][1] === k) stack.pop()
        }else{
            stack.push([char, 1])
        }
    }
    let res = ""
    for(let i = 0; i < stack.length; i++){
        res += stack[i][0].repeat(stack[i][1])
    }
    return res
};