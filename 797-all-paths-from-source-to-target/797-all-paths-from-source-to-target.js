/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {

    const ans = [];
    
    function backtrack(path){ // [0,1]
        const end = path[path.length-1];
        if(end===graph.length-1){
            ans.push(path);
            return;
        }
        
        for(const connection of graph[end]){
            backtrack([...path,connection]); // [0,1,2] and [0,1,3]
        }
    }
    
    backtrack([0]);
    
    return ans;
};