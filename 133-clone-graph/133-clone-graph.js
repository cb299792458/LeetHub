/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node, copies = {}) {
    if(!node) return
    
    if(!copies[node.val]){
        copies[node.val] = new Node(node.val,[]);    
        
        for(let neighbor of node.neighbors){
            copies[node.val].neighbors.push(cloneGraph(neighbor,copies));
        }
        
    } else {
        return copies[node.val];
    }
    
    return copies[node.val]
    
//     if(node.val){
//         let copy = new Node(node.val,[]);
//         node.val = undefined;
        
//         for(let neighbor of node.neighbors){
//             neighborCopy = cloneGraph(neighbor);
//             if(neighborCopy){
//                 copy.neighbors.push(neighborCopy);
//             }
            
//         }
        
//         console.log(copy)
//         return copy;
        
//     } else {
//         return;
//     }
    
};