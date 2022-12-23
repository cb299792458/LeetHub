/**
 * @param {number} ax1
 * @param {number} ay1
 * @param {number} ax2
 * @param {number} ay2
 * @param {number} bx1
 * @param {number} by1
 * @param {number} bx2
 * @param {number} by2
 * @return {number}
 */
var computeArea = function(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {
    const Aa = (ay2-ay1)*(ax2-ax1);
    const Ab = (by2-by1)*(bx2-bx1);
    let overlap = 0;
    
    overlapTop = Math.min(ay2,by2);
    overlapBot = Math.max(ay1,by1);
    overlapRight = Math.min(ax2,bx2);
    overlapLeft = Math.max(ax1,bx1);
    
    if(overlapTop>overlapBot && overlapRight>overlapLeft){
        overlap = (overlapTop - overlapBot) * (overlapRight - overlapLeft);
    }
    
    
    
    return Aa + Ab - Math.abs(overlap);
};