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
 
 breadth first search (QUEUE)
 5 4 8 11 13 4 7 2 1
 
 depth first search (STACK)
 5 4 11 7 2 8 13 4 1

 
 */
var hasPathSum = function(root, targetSum) {
    // base case
    if (!root) return false; // no node
    if (!root.left && !root.right) { // at leaf
        if (targetSum === root.val) { // we are at the target
            return true
        }
    }
    
    // recursive case
    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val) 

};