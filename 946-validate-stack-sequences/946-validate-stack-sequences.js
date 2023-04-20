/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
function validateStackSequences(pushed, popped) {
    let i=0;
    const stack=[];
    for(let ele of pushed){
        stack.push(ele);
        
        while(stack.length && stack.at(-1)===popped[i]){
            stack.pop();
            i++;
        }
    }
    return i===popped.length;
}
