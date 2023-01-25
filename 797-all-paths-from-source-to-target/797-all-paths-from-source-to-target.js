/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {

    const ans = [];
    
    function backtrack(path){
        const end = path[path.length-1];
        if(end===graph.length-1){
            ans.push(path);
            return;
        }
        
        for(const connection of graph[end]){
            backtrack([...path,connection]);
        }
    }
    
    backtrack([0]);
    
    return ans;
};