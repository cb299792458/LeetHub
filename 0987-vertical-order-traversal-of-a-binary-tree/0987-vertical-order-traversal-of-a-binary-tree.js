/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var verticalTraversal = function(root) {
    const nums = {};
    
    function fillMap(node,col,row){
        if(!node) return;
        if(!nums[col]) nums[col] = {};
        if(!nums[col][row]) nums[col][row] = [];
        nums[col][row].push(node.val);
        
        fillMap(node.left,col-1,row+1);
        fillMap(node.right,col+1,row+1);
    }
    
    fillMap(root,0,0);
    let colIndices = Object.keys(nums);
    colIndices.sort((a,b)=>parseInt(a)-parseInt(b));
    
    const ans = [];
    for(let colIndex of colIndices){
        let temp = [];
        
        let rowIndices = Object.keys(nums[colIndex]);
        rowIndices.sort((a,b)=>parseInt(a)-parseInt(b));
        for(let rowIndex of rowIndices){
            nums[colIndex][rowIndex].sort((a,b)=>a-b)
            temp = temp.concat(nums[colIndex][rowIndex])
        }
        
        ans.push(temp);
    }
    
    return ans;
};