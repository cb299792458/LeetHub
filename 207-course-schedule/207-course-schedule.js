/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    
    let graph = buildGraph(prerequisites);
    let res = true;
    
    const checkLoop = (id) => {
        if(seen.has(id)){
            return false;
        }
        seen.add(id);
        if(graph[id] !== undefined){
            for(let prereq of graph[id]){
                if(!checkLoop(prereq)) return false;
            }
        }
        seen.delete(id);
        graph[id] = undefined;
        return true;
    };
    
    let seen = new Set;
    for(let course = 0; course < numCourses; course++){
        if(!checkLoop(course)) return false;
    }
    return true;
        
};

function buildGraph(prerequisites) {
    const graph = {};
    for(let prereq of prerequisites){
        const [a,b] = prereq;
        
        if(!(a in graph)) graph[a] = [];
        graph[a].push(b);
    }
    return graph;
}