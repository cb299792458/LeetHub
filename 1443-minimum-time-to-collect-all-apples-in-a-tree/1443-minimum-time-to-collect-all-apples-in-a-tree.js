/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    const graph = buildGraph(edges);
    let count = -1; // Going to count every node that must be visited, except for root
    
    const checked = new Set;
    const mustVisitMemo = [];
    
    const findMustVisitNodes = (node) => {
        if(mustVisitMemo[node]!==undefined) return;
        
        if(checked.has(node)) return;
        checked.add(node);
        
        let res = false;
        
        if(hasApple[node]) res = true; // If node has an apple, it must be visited
        
        for(let neighbor of graph[node]){ // If a node's descendent has an apple, it must be visited
            if(findMustVisitNodes(neighbor)) res = true;
        }
    
        if(res) count++;
        mustVisitMemo[node] = res;
        return res;
    }

    findMustVisitNodes(0);
    // let count = -1;
    // for(let node of mustVisitMemo){
    //     if(node) count++;
    // }
    return Math.max(count*2,0);
};

const buildGraph = function(edges){
    // Make an adjacency matrix
    // index is node, element is an array of all neighbors of that node
    const res = [];
    for(let edge of edges){
        if(!res[edge[0]]) res[edge[0]] = [];
        if(!res[edge[1]]) res[edge[1]] = [];
        res[edge[0]].push(edge[1]);
        res[edge[1]].push(edge[0]);
    }
    return res;
}
