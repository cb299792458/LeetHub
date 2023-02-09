/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {

    let safe = new Set();
    
    function analyze(node, seen = new Set()){
        if(safe.has(node)) return true;
        if(seen.has(node)) return false;
        seen.add(node);
        
        if(!graph[node].length){
            safe.add(node);
            return true;
        }
        
        for(let neighbor of graph[node]){
            if(!analyze(neighbor,seen)) return false;
        }
        
        safe.add(node);
        return true;
    }
    
    let ans = [];
    for(let i=0;i<graph.length;i++){
        if(analyze(i)) ans.push(i);
    }
    return ans;
};