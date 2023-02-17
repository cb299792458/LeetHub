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
 * @return {number}
 */
var minDiffInBST = function(root) {
//     if(!root) return Infinity;
//     let left = root.left ? root.val - root.left.val : Infinity;
//     let right = root.right ? root.right.val - root.val : Infinity;
//     console.log(root.val,root.left.val)
    
//     return Math.min(minDiffInBST(root.left),minDiffInBST(root.right),left,right);
    let nums = [];
    function traverse(node){
        if(!node) return;
        nums.push(node.val);
        if(node.left) traverse(node.left);
        if(node.right) traverse(node.right);
    }
    traverse(root);
    
    // console.log(nums)
    let min = Infinity;
    for(let i=0;i<nums.length;i++){
        for(let j=i+1;j<nums.length;j++){
            min = Math.min(min,Math.abs(nums[i]-nums[j]))
        }
    }
    return min;
};
