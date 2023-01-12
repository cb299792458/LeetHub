/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    const graph = [];
    for(let i=0; i<n; i++){
        graph[i]=[];
    }
    for(const edge of edges){
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    }
    
    const res = [];
    const memo = {};
    
    const countLabel = (node) => {

        if(memo[node]) return new Array(26).fill(0);
        memo[node] = new Array(26).fill(0);
        
        for(let neighbor of graph[node]){
            const neighborCounts = countLabel(neighbor);
            for(let index in neighborCounts){
                memo[node][index] += neighborCounts[index];
            }
        }
        
        memo[node][alphabet.indexOf(labels[node])]++;
        
        res[node] = memo[node][alphabet.indexOf(labels[node])];
        return memo[node];
    };
    
    countLabel(0)
    return res
    
};