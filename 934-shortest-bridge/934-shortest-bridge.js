/**
 * @param {number[][]} grid
 * @return {number}
 */
const fill = function(image, r, c, color, prev){
    if(
        r >= 0 &&
        c >= 0 &&
        r < image.length &&
        c < image[0].length &&
        image[r][c] !== color &&
        image[r][c] === prev
    ){
        image[r][c] = color;
        fill(image, r + 1, c, color, prev);
        fill(image, r - 1, c, color, prev);
        fill(image, r, c + 1, color, prev);
        fill(image, r, c - 1, color, prev);
    }
}

var shortestBridge = function(grid) {
    let color = 'A';
    for(let r=0;r<grid.length;r++){
        for(let c=0;c<grid[0].length;c++){
            if(grid[r][c]===0) grid[r][c]="W";
            if(grid[r][c]===1){
                fill(grid,r,c,color,1);
                color='B';
            }
        }
    }
    
    let ans = Infinity;
    let queue = [];
    let seen = new Set();
    
    function backtrack(r,c,dist){
        if(r<0||c<0||r===grid.length||c===grid[0].length) return; // out of bounds
        if(seen.has(`${r},${c}`)) return; // prevent looping path
        seen.add(`${r},${c}`);
        
        if(grid[r][c]==='A'&&dist>0) return; // don't hit first island, except first step
        if(dist>ans) return; // stop when path already too long        
        
        if(grid[r][c]==='B'){
            ans=Math.min(ans,dist-1); 
            return; // save path length if shortest
        }

        queue.push([r+1,c,dist+1]);
        queue.push([r-1,c,dist+1]);
        queue.push([r,c+1,dist+1]);
        queue.push([r,c-1,dist+1]);
    }
    
    for(let r=0;r<grid.length;r++){
        for(let c=0;c<grid[0].length;c++){
            if(grid[r][c]==='A') queue.push([r,c,0]);
        }
    }
    
    while(queue.length){
        let current = queue.shift();
        backtrack(...current);
    }
    
    return ans;
};