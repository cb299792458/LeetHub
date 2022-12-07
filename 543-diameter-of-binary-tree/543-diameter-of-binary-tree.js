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
var diameterOfBinaryTree = function(root) {
    // let diameter = 0;
    // if(root.left){diameter += height(root.left)}
    // if(root.right){diameter += height(root.right)}
    // return diameter;
    
    if(!root){return 0}
    let left = diameterOfBinaryTree(root.left);
    let right = diameterOfBinaryTree(root.right);
    return Math.max(left, right, height(root.left) + height(root.right))
};


function height(root) {
    if(!root){return 0}
    return 1+Math.max(height(root.left),height(root.right));
};