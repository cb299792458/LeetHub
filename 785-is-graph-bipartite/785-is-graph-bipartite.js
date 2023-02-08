/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    const a = new Set();
    const b = new Set();
    const checked = new Set();
    
    const stack = [];
    for(let i=0;i<graph.length;i++){
        stack.unshift(i);
    }
    
    while(stack.length){
        let currentNode = stack.pop();
        
        if(checked.has(currentNode)){
            continue;
        } else {
            checked.add(currentNode);
        }
        
        let currentSet;
        let otherSet;
        
        if(!b.has(currentNode)){
            a.add(currentNode);
            currentSet = a;
            otherSet = b;
        } else {
            b.add(currentNode);
            currentSet = b;
            otherSet = a;
        }
        
        for(let connection of graph[currentNode]){
            if(currentSet.has(connection)){
                // console.log(a,b);
                return false;
            } else {
                otherSet.add(connection);
                stack.push(connection);
            }
        }
        
    }
    
    return true;
};