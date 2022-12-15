/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let queue = [];
    const inBounds = (row,col)=>{
        return row >= 0 && row < grid.length && col >= 0 && col < grid[0].length;
    }
    for(let row = 0; row < grid.length; row++){
        for(let col = 0; col < grid[0].length; col++){
            if(grid[row][col] === 2){
                queue.push([row,col,0]);
            }
        }
    }
    
    let longestTime = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    while(queue.length > 0){
        const [row,col,minutes] = queue.shift();
        for(let dir of dirs){
            
            const newRow = row + dir[0];
            const newCol = col + dir[1];

            if(inBounds(newRow,newCol) && grid[newRow][newCol] !== 2 && grid[newRow][newCol] !== 0){
                queue.push([newRow,newCol,minutes+1]);
                longestTime = Math.max(longestTime, minutes+1);
                grid[newRow][newCol] = 2;
            }
        }
    }
    
    for(let row = 0; row < grid.length; row++){
        for(let col = 0; col < grid[0].length; col++){
            if(grid[row][col]===1) return -1;
        }
    }
    
    return longestTime;
    
};