/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    let graph = buildGraph(prerequisites);
    let order = [];
    let taken = new Set();
    console.log(graph, graph[0], graph[1])
    
    
    let tookNewCourse = true;
    while(tookNewCourse){
        tookNewCourse = false;
        for(let i=0;i<numCourses;i++){
            if(taken.has(i)) continue;
            
            if(!graph[i]){
                tookNewCourse = true;
                taken.add(i);
                order.push(i);
                continue;
            }
            
            let canTake = true;
            for(let prereq of graph[i]){
                if(!taken.has(prereq)) canTake = false;
            }
            if(!canTake) continue;
            tookNewCourse = true;
            taken.add(i);
            order.push(i);
        }
    }
    
    
    return order.length===numCourses ? order : [];
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