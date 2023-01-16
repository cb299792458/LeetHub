/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    const a = new Set;
    const b = new Set;
    const checked = new Set;
    
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
                console.log(a,b);
                // console.log("Returning false because ", i, connection, ' are in the same set')
                return false;
            } else {
                otherSet.add(connection);
                stack.push(connection);
            }
        }
        
    }
    
    
    
//     for(let i=0;i<graph.length;i++){
//         // add first node to a set
//         let currentSet;
//         let otherSet;
        
//         if(!b.has(i)){
//             a.add(i);
//             currentSet = a;
//             otherSet = b;
//         } else {
//             b.add(i);
//             currentSet = b;
//             otherSet = a;
//         }
        
        
//         // return false if connection is already in first set
//         // add first node's connections to other set
//         for(let connection of graph[i]){
//             if(currentSet.has(connection)){
//                 console.log(a,b);
//                 console.log("Returning false because ", i, connection, ' are in the same set')
//                 return false;
//             } else {
//                 otherSet.add(connection);
//             }
//         }
    
    // };
    
    // return true if you got through all edges in graph
    return true;
};