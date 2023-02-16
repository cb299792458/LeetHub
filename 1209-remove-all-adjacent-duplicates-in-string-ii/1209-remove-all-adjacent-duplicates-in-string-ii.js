/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function(s, k) {
    
    // make a stack = []
    let stack = [];
    
    // for loop
    for(let i=0;i<s.length;i++){
        // put char in the stack
        let char = s[i];
        stack.push(char);
        
        
        // check if the last k elements in the stack are the same;
        if(stack.length >= k){
            let lastK = stack.slice(stack.length-k);
            // console.log(lastK)
            if( lastK.every((element) => element === stack.at(-1)) ){
                for(let i=0;i<k;i++) stack.pop();
            } 
        }
        
    }
    return stack.join('');
    
};


// aa
