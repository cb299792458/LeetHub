/**
 * @param {number[][]} grid
 * @return {number}
 */
var floodFill = function(image, sr, sc, color) {
    fill(image, sr, sc, color, image[sr][sc])
    return image;
};

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
    // console.log(grid);
    
    let ans = Infinity;
    let queue = [];
    
    function backtrack(r,c,dist, seen = new Set() ){
        // console.log(r,c)
        if(r<0||c<0||r===grid.length||c===grid[0].length) return;
        if(seen.has(`${r},${c}`)) return;
        seen.add(`${r},${c}`);
        
        if(grid[r][c]==='A'&&dist>0) return;
        if(dist>ans) return;        
        
        if(grid[r][c]==='B'){
            ans=Math.min(ans,dist-1);
            return;
        }
        
        // backtrack(r+1,c,dist+1,new Set(seen));
        // backtrack(r,c+1,dist+1,new Set(seen));
        // backtrack(r-1,c,dist+1,new Set(seen));
        // backtrack(r,c-1,dist+1,new Set(seen));
        
        queue.push([r+1,c,dist+1,seen]);
        queue.push([r-1,c,dist+1,seen]);
        queue.push([r,c+1,dist+1,seen]);
        queue.push([r,c-1,dist+1,seen]);
        
        while(queue.length){
            let current = queue.shift();
            backtrack(...current);
        }
    }
    
    
    for(let r=0;r<grid.length;r++){
        for(let c=0;c<grid[0].length;c++){
            if(grid[r][c]==='A') backtrack(r,c,0);
        }
    }
    
    return ans;
};