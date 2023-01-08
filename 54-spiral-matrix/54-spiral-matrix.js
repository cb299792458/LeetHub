/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
    let dirIdx = 0;
    const rows = matrix.length;
    const cols = matrix[0].length;
    
    // Set up boundary around matrix
    let out = [];
    for(let i = -1; i <= rows; i ++){
        for(let j = -1; j <= cols; j ++){
            if(i===-1 || j===-1 || i===rows || j===cols){
                out.push(`${i},${j}`);
            }
        }
    }
    
    let [r,c] = [0,0];
    let res = [];
    while(res.length < rows*cols){
        
        // Add new element to res
        if(!out.includes(`${r},${c}`)){
            out.push(`${r},${c}`);
            res.push(matrix[r][c]);
        }
        
        
        [r,c] = [r+dirs[dirIdx%4][0],c+dirs[dirIdx%4][1]];
        if(out.includes(`${r},${c}`)){
            [r,c] = [r-dirs[dirIdx%4][0],c-dirs[dirIdx%4][1]];
            dirIdx++;
        }
        
    }
    
    return res;
};