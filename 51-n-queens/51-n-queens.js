/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const ans = [];
       
    function parse(grid){
        let res = [];
        for(let i=0;i<n;i++){
            res.push(grid[i].join(''));
        }
        return res;
    }
    
    function backtrack(grid,queens=0,rows=new Set,cols=new Set,sumdiags=new Set,difdiags=new Set){
        let row = queens;
        if(queens===n){
            let parsed = parse(grid);

            ans.push(parsed);

            return;
        }
        
        rows = new Set(rows);
        cols = new Set(cols);
        sumdiags = new Set(sumdiags);
        difdiags = new Set(difdiags);
        grid.push(new Array(n).fill('.'))
        
        for(let col=0;col<n;col++){
            if(rows.has(row)||cols.has(col)||sumdiags.has(row+col)||difdiags.has(row-col)) continue;

            rows.add(row);
            cols.add(col);
            sumdiags.add(row+col);
            difdiags.add(row-col);    
            grid[row][col] = 'Q';
            backtrack(grid,queens+1,rows,cols,sumdiags,difdiags);

            rows.delete(row);
            cols.delete(col);
            sumdiags.delete(row+col);
            difdiags.delete(row-col);  
            grid[row][col] = '.';
        }
    }
    
    backtrack([],0);
    
    return ans;
    
};