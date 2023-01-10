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
        
    } 
    
    return copies[node.val]
    
};