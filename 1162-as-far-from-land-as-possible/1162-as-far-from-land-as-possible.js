/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function(grid) {
    let max = 0;
    let dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    let queue = [];
    let hasWater = false;
    let seen = new Set()
    
    function fill(r,c,dist){
        if(r<0||c<0||r===grid.length||c===grid.length) return;
        if(seen.has(`${r},${c}`)) return;
        seen.add(`${r},${c}`);
        
        if(grid[r][c] === 0) hasWater = true;
        grid[r][c] = dist;
        
        for(let dir of dirs){
            let [nr,nc] = [r+dir[0],c+dir[1]];
            if(nr<0||nc<0||nr===grid.length||nc===grid.length) continue;

            if(grid[nr][nc] !== 1) queue.push([nr,nc,dist+1]);
        } 
    }
    
    for(let r=0;r<grid.length;r++){
        for(let c=0;c<grid[0].length;c++){
            if(grid[r][c]===1){
                queue.push([r,c,1])
            }
        }
    }
    if(!queue.length) return -1;
    
    while(queue.length){
        let current = queue.shift();
        fill(...current);
    }
    
    for(let r=0;r<grid.length;r++){
        for(let c=0;c<grid[0].length;c++){
            max = Math.max(max,grid[r][c])
        }
    }
        
    return hasWater ? max-1 : -1;
};