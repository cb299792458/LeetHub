class SubrectangleQueries {
    constructor(grid){
        this.grid = grid;
    }
    
    updateSubrectangle(r1,c1,r2,c2,val){
        for(let r=r1;r<=r2;r++){
            for(let c=c1;c<=c2;c++){
                this.grid[r][c] = val;
            }
        }
    }
    
    getValue(r,c){
        return this.grid[r][c];
    }
}