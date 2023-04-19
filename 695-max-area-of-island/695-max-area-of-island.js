/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    let set = new Set();
    let max = 0;
    
    
    for(let r = 0; r<grid.length;r++){
        for(let c = 0; c < grid[0].length; c++){
            max = Math.max(max,dfs(grid,r,c,set));
        }
    }
    
    return max;
    
};

function dfs(grid,row,col,visited){
    if(row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || visited.has(`${row},${col}`) || grid[row][col] === 0){
        return 0;
    }
    
    visited.add(`${row},${col}`);
    
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    
    let count = 1;
    
    for(let dir of dirs){
        const newRow = row + dir[0];
        const newCol = col + dir[1];
        count += dfs(grid,newRow,newCol,visited);
    }
    
    return count;
}