/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    let taskDict = {};
    for(let task of tasks){
        if(!taskDict[task]) taskDict[task] = {count: 0, cooldown: 0};
        taskDict[task].count++;
    }
    
    let res = 0;
    while(true){
        let mostTask = false;
        let mostNum = 0;
        for(let task in taskDict){
            if(taskDict[task].count===0){
                delete taskDict[task];
                continue;
            }
            
            // console.log(taskDict[task])
            if(taskDict[task].count>mostNum && taskDict[task].cooldown<=0){
                mostTask = task;
                mostNum = taskDict[mostTask].count;
            }
            taskDict[task].cooldown--;
        }
        
        if(!Object.values(taskDict).length) break;
        
        res++;
        if(!mostTask) continue;
        taskDict[mostTask].count--;
        taskDict[mostTask].cooldown = n;
        
    }
    return res;
};