/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    let al = makeAdjacencyList(edges);
    console.log(al)

    let nodes = new Set();
    for(let i=0;i<n;i++) nodes.add(i);
    // console.log(nodes);
    
    while(nodes.size>2){
        let queue = [];
        
        for(let node of nodes) if(al[node].size===1) queue.push(node);
        
        for(let node of queue){
            for(let a of al[node]){
                al[a].delete(node);
            }
            nodes.delete(node);
        }

    }
    // console.log(nodes)
    return Array.from(nodes);
}

function makeAdjacencyList(edges){
    const adjacencies = [];
    for(let edge of edges){
        if(!adjacencies[edge[0]]) adjacencies[edge[0]] = new Set();
        adjacencies[edge[0]].add(edge[1]);
        if(!adjacencies[edge[1]]) adjacencies[edge[1]] = new Set();
        adjacencies[edge[1]].add(edge[0]);
    }
    return adjacencies;
}