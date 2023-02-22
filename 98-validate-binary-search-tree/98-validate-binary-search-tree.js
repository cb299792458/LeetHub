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
 * @return {boolean}
 */
var isValidBST = function(root, max = Infinity, min = -Infinity) {
    if(!root) return true;
    if(root.val >= max || root.val <= min) return false;
    // let newMax = Math.min(max,root.val);
    // let newMin = Math.max(min,root.val);
    return(isValidBST(root.left,root.val,min) && isValidBST(root.right,max,root.val));
};