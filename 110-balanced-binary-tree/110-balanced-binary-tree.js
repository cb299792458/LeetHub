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
var isBalanced = function(root) {
    if(!root){ return true }
    return nodeIsBalanced(root) && isBalanced(root.right) && isBalanced(root.left)
};

const height = (root) => {
    if(!root){ return 0 }

    if(!root.left && !root.right){
        return 1;
    } else {
        return Math.max(height(root.left),height(root.right)) + 1;
    }
}

const nodeIsBalanced = function(root) {
    // if(!root){ return true }

    const left = root.left ? height(root.left) : 0;
    const right = root.right ? height(root.right) : 0;
    return Math.abs( left - right ) < 2;
}