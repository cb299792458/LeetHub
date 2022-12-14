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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum, currSum = 0) {
    if(!root) return false
    currSum += root.val
    if(targetSum === currSum && !root.left && !root.right) return true
    return hasPathSum(root.left, targetSum, currSum) || hasPathSum(root.right, targetSum, currSum)
};